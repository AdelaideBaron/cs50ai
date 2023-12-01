import unittest
from tictactoe import player
from tictactoe import actions
from tictactoe import result
import tictactoe

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

    def test_result_applies_action_to_board_for_X_next(self):
        action_to_apply = (2,1)
        board_to_use = self.empty_board
        expected_result = [[self.EMPTY, self.EMPTY, self.EMPTY],
                           [self.EMPTY, self.EMPTY, self.EMPTY],
                           [self.EMPTY, self.X, self.EMPTY]]
        actual = result(board_to_use,action_to_apply)
        self.assertEqual(expected_result, actual)

    def test_result_applies_action_to_board_for_O_next(self):
        action_to_apply = (2,1)
        board_to_use = self.O_next
        expected_result = [[self.O, self.EMPTY, self.X],
                           [self.EMPTY, self.O, self.EMPTY],
                           [self.X, self.O, self.X]]
        actual = result(board_to_use,action_to_apply)
        self.assertEqual(expected_result, actual)

    def test_get_possible_wins_for_populated_cell(self):
        possible_moves = [
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], #horizontal
            [(0,0), (1,0), (2,0)], [(0,1), (1,1),(2,1)], [(0,2),(1,2),(2,2)], #vertical
            [(0,0), (1,1),(2,2)], [(0,2), (1,1), (2,0)] #diagonal
        ]
        expected_possible_wins = [
            [(0,0), (0,1), (0,2)],
            [(0,0), (1,0), (2,0)],
            [(0,0), (1,1),(2,2)]
        ]
        self.assertEqual(sorted(expected_possible_wins), sorted(tictactoe.get_possible_wins(possible_moves, (0,0), True)))

    def test_get_possible_wins_for_unpopulated_cell(self):
        possible_moves = [
        [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], #horizontal
        [(0,0), (1,0), (2,0)], [(0,1), (1,1),(2,1)], [(0,2),(1,2),(2,2)], #vertical
        [(0,0), (1,1),(2,2)], [(0,2), (1,1), (2,0)] #diagonal
        ]
        expected_possible_wins = [

         [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], #horizontal
             [(0,1), (1,1),(2,1)], [(0,2),(1,2),(2,2)], #vertical
         [(0,2), (1,1), (2,0)] #diagonal
        ]
        print(tictactoe.get_possible_wins(possible_moves, (0,0), True) )
        self.assertEqual(sorted(expected_possible_wins), sorted(tictactoe.get_possible_wins(possible_moves, (0,0), False)))

if __name__ == '__main__':
    unittest.main()