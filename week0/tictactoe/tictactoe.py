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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()

    for i, row in enumerate(board):
        for j, entry in enumerate(row):
            if entry == EMPTY:
                available_actions.add((i, j))

    return available_actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    next_player = player(board)
    board[action[0]][action[1]] = next_player

    return board
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
