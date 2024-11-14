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
    x_count = 0
    o_count = 0

    for row in board:
        for col in board[row]:
            if board[row][col] == X:
                x_count += 1
            elif board[row][col] == O:
                o_count += 1

    if x_count >= o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in board:
        for col in board[row]:
            if board[row][col] != X and board[row][col] != O:
                possible_actions.add((row,col))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not is_valid_action(action) or not is_valid_board_field(action, board):
        raise ValueError
    
    new_board = board.copy()
    row = action[0]
    col = action[1]

    new_board[row][col] = player(board)

    return new_board


def is_valid_board_field(action, board):
    
    return board[action[0]][action[1]] == None

def is_valid_action(action):
    return is_valid_action_size(action) and is_valid_action_values(action)

def is_valid_action_size(action):
    return len(action) == 2

def is_valid_action_values(action):
    return action[0] not in (0,1,2) and action[1] not in (0,1,2)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #check cross
    is_cross_00_winner = board[0][0] == board[1][1] == board[2][2] and board[0][0] != None
    is_cross_20_winner = board[2][0] == board[1][1] == board[0][2] and board[2][0] != None
    
    if is_cross_00_winner:
        return board[0][0]
    if is_cross_20_winner:
        return board[2][0]

    #check horizontal and vertical
    for i in range(3):
        row = board[i]
        is_horizontal_winner = row[0] == row[1] == row[2] and row[0] != None
        is_vertical_winner = board[0][i] == board[1][i] == board [2][i] and board[0][i] != None

        if is_horizontal_winner:
            return row[0]
        if is_vertical_winner:
            return board[0][i]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None or is_all_field_filled(board)

def is_all_field_filled(board):
    for row in board:
        for col in row:
            if board[row][col] == None:
                return False
    return True


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
