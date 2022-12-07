"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
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
    count_x =0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            if cell == O:
                count_o += 1
    if count_x<=count_o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            action.add((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in action(board):
        raise ValueError
    else:
        new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(new_board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for _ in [0,1,2]:
        if board[_] == [X,X,X]:
            return X
        elif board[_] == [O,O,O]:
            return O
        for __ in [0,1,2]:
            if board[__][_] == X:
                return X
            elif board[__][_] == O:
                return O
    if ((board[1][1] == X) and (board[2][2] == X) and (board[3][3] == X)) or ((board[1][3] == X) and (board[2][2] == X) and (board[3][1] == X)):
        return X
    elif ((board[1][1] == O) and (board[2][2] == O) and (board[3][3] == O)) or ((board[1][3] == O) and (board[2][2] == O) and (board[3][1] == O)):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False

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

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if terminal(board):
        return None
    elif board == initial_state():
        return 1,2
    else:
        current_value = float("-inf") if current_player == X else float("-inf")
        for action in actions(board):
            new_value = min_max_value(result(board,action), current_value)
        if current_player == X:
            new_value = max(current_value,new_value)
        if current_player == O:
            new_value = min(current_value,new_value)
        
        if new_value != current_value:
            best_value = new_value
            best_action = action
        return best_action
        
def min_max_value(board,action):
    if terminal(board):
        return utility(board)

    current_player = player(board)
    value = float("-inf") if current_player == X else float("inf")

    for action in actions(board):
        new_value = min_max_value(result(board, action), value)

        if current_player == X:
            if new_value > value:
                return new_value
            value = max(value, new_value)

        if current_player == O:
            if new_value < value:
                return new_value
            value = min(value, new_value)

    return value