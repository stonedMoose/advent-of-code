import unittest

from day4.Board import Board

BOARD = [
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34],
    [40, 41, 42, 43, 44],
    [50, 51, 52, 53, 54],
]

class BoardTest(unittest.TestCase):



    def test_should_not_build_without_5_row(self):
        self.assertRaises(Exception, lambda: Board([]))

    def test_should_not_build_without_5_row_of_5_column(self):
        self.assertRaises(Exception, lambda: Board([
            [],
            [],
            [],
            [],
            []
        ]))

    def test_have_all_number_not_drawn_at_start(self):
        board = Board(BOARD)

        for i, _ in enumerate(BOARD):
            for j, _ in enumerate(BOARD):
                self.assertFalse(board.is_drawn(i, j))

    def test_should_drawn_case(self):
        board = Board(BOARD)

        board.draw(10)

        self.assertTrue(board.is_drawn(0, 0))

    def test_should_tell_if_won_when_line_complete(self):
        board = Board(BOARD)

        board.draw(10)
        self.assertFalse(board.is_won())
        board.draw(11)
        self.assertFalse(board.is_won())
        board.draw(12)
        self.assertFalse(board.is_won())
        board.draw(13)
        self.assertFalse(board.is_won())
        board.draw(14)
        self.assertTrue(board.is_won())

    def test_should_tell_if_won_when_column_complete(self):
        board = Board(BOARD)

        board.draw(10)
        self.assertFalse(board.is_won())
        board.draw(20)
        self.assertFalse(board.is_won())
        board.draw(30)
        self.assertFalse(board.is_won())
        board.draw(40)
        self.assertFalse(board.is_won())
        board.draw(50)
        self.assertTrue(board.is_won())


    def test_should_tell_not_whon_when_diagonale(self):
        board = Board(BOARD)

        board.draw(10)
        self.assertFalse(board.is_won())
        board.draw(21)
        self.assertFalse(board.is_won())
        board.draw(32)
        self.assertFalse(board.is_won())
        board.draw(43)
        self.assertFalse(board.is_won())
        board.draw(54)
        self.assertFalse(board.is_won())

    def test_compute_undrawn_total(self):
        board = Board(BOARD)

        self.assertEqual(board.get_undrawn_total(), 800)
        board.draw(10)
        self.assertEqual(board.get_undrawn_total(), 790)
        board.draw(21)
        self.assertEqual(board.get_undrawn_total(), 769)
        board.draw(32)
        self.assertEqual(board.get_undrawn_total(), 737)
        board.draw(43)
        self.assertEqual(board.get_undrawn_total(), 694)
        board.draw(54)
        self.assertEqual(board.get_undrawn_total(), 640)
