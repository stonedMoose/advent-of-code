from day4.Board import Board
from get_lines import get_lines


class Bingo:

    def __init__(self, inputs):
        lines = get_lines(inputs)
        self.boards = []
        self.build_boards(lines)
        self.draws = self.get_draws(lines)
        self.current_draw = None

    def build_boards(self, lines):
        board_values = []
        for line in list(map(lambda a_line: a_line.strip(), lines[1:])):
            if line != '':
                row = list(map(lambda a: int(a.strip()), line.split()))
                board_values.append(row)
            if len(board_values) == 5:
                self.boards.append(Board(board_values))
                board_values = []

    def get_draws(self, lines):
        return map(lambda a: int(a), lines[0].split(','))

    def get_first_board_to_win_score(self):
        for draw in self.draws:
            for board in self.boards:
                board.draw(draw)
                if board.is_won():
                    return self.get_bingo_score(board, draw)

    def get_last_board_to_win_score(self):
        for draw in self.draws:
            for board in self.boards:
                board.draw(draw)
                if len(list(filter(lambda b: not b.is_won(), self.boards))) == 0:
                    return self.get_bingo_score(board, draw)

    def get_bingo_score(self, board: Board, draw: int):
        return board.get_undrawn_total() * draw