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


# The winner function should accept a board as input, and return the winner of the board if there is one.
# If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
# One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
# You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
# If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
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

    # check 1,1 first - as thats one of the most common
    if board[1][1] == player_to_check:
        possible_wins = get_possible_moves(possible_wins, (1, 1), True)
    else:
        possible_wins = get_possible_moves(possible_wins, (1, 1), False)

    for combination in possible_wins: #don't feel this properly enumerates over what gets updated in lower lines
        i = combination[0][0]
        j = combination[0][1]
        if board[i][j] == player_to_check:
            # check if winner
            i = combination[1][0]
            j = combination[1][1]
            if board[i][j] == player_to_check:
                i = combination[2][0]
                j = combination[2][1]
                if board[i][j] == player_to_check:
                    print('WINNING COMBO FOUND')
                    winner = True
                    break
                else:
                    possible_wins = get_possible_moves(possible_wins, (i, j), False)
                    break #is necessary?
            else:
                possible_wins = get_possible_moves(possible_wins, (i, j), False)
                break #is necessary?
            # otherwise, remove this & other cells from the possible_moves
            # possible_wins = get_possible_moves(possible_wins, (i, j), True)
        else:
            possible_wins = get_possible_moves(possible_wins, (i, j), False)
    return winner
    # print("HI {}".format(len(possible_wins)))
    # # check combination for winning combo
    # for combination in possible_wins:
    #
    #
    #
    # if(len(possible_wins) ==1):
    #     print(player_to_check)
    #     print(possible_wins)
    #     winning_combo = True
    #     combination = possible_wins[0]
    #     for cell in combination:
    #         i = cell[0]
    #         j = cell[1]
    #         if board[i][j] != player_to_check:
    #             winning_combo = False
    #             break
    #     return winning_combo

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
