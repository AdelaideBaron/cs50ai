import unittest
from tictactoe import player
from tictactoe import actions

class TestBoardHelpers(unittest.TestCase):
    def setUp(self):
        self.X = "X"
        self.O = "O"
        self.EMPTY = None
        self.empty_board = [[self.EMPTY, self.EMPTY, self.EMPTY],
                        [self.EMPTY, self.EMPTY, self.EMPTY],
                        [self.EMPTY, self.EMPTY, self.EMPTY]]

        self.X_next = [[self.O, self.EMPTY, self.EMPTY],
                   [self.EMPTY, self.O, self.EMPTY],
                   [self.X, self.EMPTY, self.X]]

        self.O_next = [[self.O, self.EMPTY, self.X],
                   [self.EMPTY, self.O, self.EMPTY],
                   [self.X, self.EMPTY, self.X]]

        self.X_win = [[self.O, self.EMPTY, self.EMPTY],
                  [self.EMPTY, self.O, self.EMPTY],
                  [self.X, self.X, self.X]]

    def test_player(self):
        self.assertEqual(self.X,player(self.empty_board))
        self.assertEqual(self.X, player(self.X_next))
        self.assertEqual(self.O, player(self.O_next))

    def test_empty_actions_returns_all_cells(self):
        actual_results = actions(self.empty_board)
        expected_results = {(0,0),(0, 1), (0,2), (1, 0),(1,1) ,(1, 2),(2,0), (2,1),(2, 1), (2, 2)}
        self.assertEqual(expected_results, actual_results)

    def test_actions_returns_all_cells(self):
        actual_results = actions(self.O_next)
        expected_results = {(0, 1), (1, 0), (1, 2), (2, 1)}
        self.assertEqual(expected_results, actual_results)
        # flesh this test out

if __name__ == '__main__':
    unittest.main()