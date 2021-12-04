VALUE = 'value'
DRAWN = 'drawn'


def assertBoardIsValid(board):
    if len(board) != 5:
        raise Exception('Need 5 line ine a board of bingo')
    for row in board:
        if len(row) != 5:
            raise Exception('Need 5 column in each line in a board of bingo')


class Board:

    def __init__(self, board: [str]):
        assertBoardIsValid(board)

        self.board = {}

        for i, row in enumerate(board):
            for j, column in enumerate(row):
                self.board[self.get_key(i, j)] = ({
                    VALUE: column,
                    DRAWN: False
                })

    def get_key(self, i, j):
        return "{}{}".format(i, j)

    def is_drawn(self, line_index, column_index):
        return self.board[self.get_key(line_index, column_index)][DRAWN]

    def draw(self, value):
        for case in self.board.values():
            if case[VALUE] == value:
                case[DRAWN] = True
                break

    def is_won(self):
        return self.is_any_column_complete() or self.is_any_line_complete()

    def is_any_line_complete(self):
        for line_index in range(5):
            if self.is_line_complete(line_index, 0):
                return True
        return False

    def is_any_column_complete(self):
        for column_index in range(5):
            if self.is_column_complete(0, column_index):
                return True
        return  False

    def is_line_complete(self, line_index, column_index):
        if self.board[self.get_key(line_index, column_index)][DRAWN]:
            if column_index == 4:
                return True
            return self.is_line_complete(line_index, column_index + 1)
        return False

    def is_column_complete(self, line_index, column_index):
        if self.board[self.get_key(line_index, column_index)][DRAWN]:
            if line_index == 4:
                return True

            return self.is_column_complete(line_index + 1, column_index)
        return False

    def get_undrawn_total(self):
        return sum(map(lambda case: case[VALUE], filter(lambda case: not case[DRAWN], self.board.values())))
