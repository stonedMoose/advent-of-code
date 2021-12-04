import os

from day4.Bingo import Bingo

if __name__ == '__main__':
    bingo = Bingo(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'input.txt'
        )
    )
    print('score', bingo.get_last_board_to_win_score())