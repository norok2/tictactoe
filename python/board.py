import numpy as np


def make_board(row, col):
    return np.zeros((row, col), dtype=int)


def is_empty(board):
    return np.sum(board != 0) == 0


def is_full(board):
    return np.sum(board == 0) == 0


def is_valid_move(board, row, col):
    shape = board.shape
    return (0 <= row < shape[0]) and (0 <= col < shape[1])
    # : alternate implementation,  easier to generalize to N-dims
    # return all([0 <= x < dim for x, dim in zip((row, col), board.shape)])


def is_avail_move(board, row, col):
    return board[row, col] == 0


def avail_moves(board):
    return list(zip(*np.where(board == 0)))


def do_move(board, row, col, turn):
    if is_valid_move(board, row, col) and is_avail_move(board, row, col):
        board[row, col] = turn
    else:
        print(f'Move ({row}, {col}) is invalid')
    return board


def undo_move(board, row, col):
    if is_valid_move(board, row, col) and is_avail_move(board, row, col):
        board[row, col] = 0
    else:
        print(f'No move in ({row}, {col})')
    return board


def is_winner(board, turn):
    # horizontal
    for i in range(board.shape[0]):
        if np.all(board[i, :] == turn):
            return True
    # vertical
    for j in range(board.shape[1]):
        if np.all(board[:, j] == turn):
            return True
    # diagonals
    return np.all(np.diag(board) == turn) \
           or np.all(np.diag(board[:, ::-1] == turn))
