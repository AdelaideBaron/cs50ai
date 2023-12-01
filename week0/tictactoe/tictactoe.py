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

    player_to_check = X if player(board) == O else O
    other_player = O if player_to_check == X else X

    if check_win_for_given_player(board,player_to_check):
        return player_to_check
    elif check_win_for_given_player(board,other_player):
        return other_player
    else:
        return None


    #  there will be a better way with numbers perhaps.
    # 1 2 3
    # 4 5 6
    # 7 8 9



    return None #this happens tho
    raise NotImplementedError

def check_win_for_given_player(board, player_to_check):
    winner = False
    possible_wins = [
        [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], #horizontal
        [(0,0), (1,0), (2,0)], [(0,1), (1,1),(2,1)], [(0,2),(1,2),(2,2)], #vertical
        [(0,0), (1,1),(2,2)], [(0,2), (1,1), (2,0)] #diagonal
    ]

    if board[1][1] == player_to_check:
        possible_wins = get_possible_moves(possible_wins, (1, 1), True)
    else:
        possible_wins = get_possible_moves(possible_wins, (1, 1), False)

    for combination in possible_wins:
        for pos in combination:
            i, j = pos
            if board[i][j] != player_to_check:
                possible_wins = get_possible_moves(possible_wins, (i, j), False)
                break
        else:
            print('WINNING COMBO FOUND')
            winner = True

    return winner

def get_possible_moves(possible_moves, cell, is_populated):
    moves_to_return = list()
    if is_populated:
        for combination in possible_moves:
            if cell in combination:
                moves_to_return.append(combination)
    elif not is_populated:
        for combination in possible_moves:
            if cell not in combination:
                moves_to_return.append(combination)
    return moves_to_return

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
