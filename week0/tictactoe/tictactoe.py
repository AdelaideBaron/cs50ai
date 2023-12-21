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

possible_wins = [
    [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], #horizontal
    [(0,0), (1,0), (2,0)], [(0,1), (1,1),(2,1)], [(0,2),(1,2),(2,2)], #vertical
    [(0,0), (1,1),(2,2)], [(0,2), (1,1), (2,0)] #diagonal
]

def check_win_for_given_player(board, player_to_check):
    winner = False
    global possible_wins

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

def get_possible_moves(possible_moves, cell, is_populated): #empty combos, cell to check, if you want wins including or excluding this cell

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
    # check for a winner
    if winner(board) != None:
        return True
    # check for NO empties
    for row in board:
        if EMPTY in row:
            return False

    return True
    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


# The minimax function should take a board as input, and return the optimal move for the player to move on that board.
# The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
# If the board is a terminal board, the minimax function should return None.
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    board_to_assess = board
    next_player = player(board_to_assess)
    possible_actions = actions(board_to_assess)
    print("board: {}".format(board))
    print("possible actions: {}".format(possible_actions))

    minimise = next_player == O

    move_values = [] #store action, optimal value[utility,moves_to_achieve
    for action in possible_actions:
        move_values.append([action, find_minmax_for_action(action, board, minimise)])

    action = None
    achievable_utility = None
    amount_of_moves = None

    if minimise:
        print('minimising')
        for combination in move_values:
            print(combination)
            possible_action = combination[0]
            utility_to_get  = combination[1][0]
            amount_of_moves_to_achieve = combination[1][1]
            if achievable_utility is None:
                amount_of_moves = amount_of_moves_to_achieve
                achievable_utility = utility_to_get
                action = possible_action
            elif utility_to_get <= achievable_utility:
                if amount_of_moves_to_achieve < amount_of_moves:
                    amount_of_moves = amount_of_moves_to_achieve
                    achievable_utility = utility_to_get
                    action = possible_action
    else:
        print('move {}'.format(move_values))
        for combination in move_values:
            possible_action = combination[0]
            utility_to_get  = combination[1][0]
            amount_of_moves_to_achieve = combination[1][1]
            if achievable_utility is None:
                amount_of_moves = amount_of_moves_to_achieve
                achievable_utility = utility_to_get
                action = possible_action
            elif utility_to_get >= achievable_utility:
                if amount_of_moves_to_achieve < amount_of_moves:
                    amount_of_moves = amount_of_moves_to_achieve
                    achievable_utility = utility_to_get
                    action = possible_action

    return action

# def recursive_action(board, move_values): #initial use move_values = []
#     possible_actions = actions(board)
#     for action in possible_actions:
#         working_board = result(board, action)
#         if terminal(working_board):
#             move_values.append([action, utility(working_board)])
#             return move_values
#         else:
#             return recursive_action(working_board, move_values)

def find_minmax_for_action(action, board, minimse):  #returns minimum/max_utility, min amount of moves to get there  #perhaps also add amount of moves to get there - then take least amount (from the list of those with utility = min/max)
    boardy = result(board, action)

    if terminal(boardy): #if the action results in an immediate terminal board
        return [utility(boardy), 1]

    possible_actions = list(actions(boardy))

    possible_actions_and_board = [] #board, action, no_of_moves
    for action in possible_actions:
        possible_actions_and_board.append([boardy, action, 1])


    utility_no_of_moves = {} #utility, no_of_moves
    # for combo in possible_actions_and_board:
    while possible_actions_and_board: #whilst there are still actions to assess
        # print("possible acions: {}".format(possible_actions_and_board))
        combo = possible_actions_and_board[0] #get the action
        print('action: ')
        possible_actions_and_board.remove(combo) #remove it from ones to address
        boardy = combo[0]
        action = combo[1]
        no_of_moves = combo[2]
        working_board = result(boardy, action)

        if terminal(working_board):
            utility_value = utility(working_board)
            if utility_value in utility_no_of_moves: #this isn't going to work? is it?
                if utility_no_of_moves[utility_value] > no_of_moves:
                    utility_no_of_moves[utility_value] = no_of_moves #update the amount of moves needed to get this utility
            else:
                utility_no_of_moves[utility_value] = no_of_moves

        else:
            possible_actions_now = list(actions(working_board))
            for action in possible_actions_now:
                possible_actions_and_board.append([working_board, action, no_of_moves +1])

    print('utilities and no of moves {}'.format(utility_no_of_moves) )
    print('minimise: {}'.format(minimse))
    if minimse:
        utility_value = min(utility_no_of_moves.keys())
        return [utility_value, utility_no_of_moves[utility_value]]
    else:
        utility_value = max(utility_no_of_moves.keys())
        return [utility_value, utility_no_of_moves[utility_value]]