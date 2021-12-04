import os.path
import unittest

from day4.Bingo import Bingo


class BingoTest(unittest.TestCase):

    test_input = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../test_input_part_1.txt'
    )
    bingo = Bingo(test_input)

    def test_first_bingo_score(self):
        self.assertEqual(self.bingo.get_first_board_to_win_score(), 4512)

    def test_last_bingo_score(self):
        self.assertEqual(self.bingo.get_last_board_to_win_score(), 1924)