import unittest
from tictactoe import player

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
        self.assertEqual(player(self.empty_board), self.X)
        self.assertEqual(player(self.X_next), self.X)
        self.assertEqual(player(self.O_next), self.O)

if __name__ == '__main__':
    unittest.main()