"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    board_sum = 0

    for row in board:
        for entry in row:
            board_values = {X: -1, O: 1}
            board_sum += board_values.get(entry, 0)

    return X if board_sum >= 0 else O

    raise NotImplementedError


# Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
# Possible moves are any cells on the board that do not already have an X or an O in them.
# Any return value is acceptable if a terminal board is provided as input.
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # 1. assess whose turn
    next_player = player(board)
    # find all empty cells
    available_actions = {}
    for row in board:
        for entry in row:
            if entry == EMPTY:
                i = board.index(row)
                j = row.index(entry)
                available_actions.add((i,j))

    return available_actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
