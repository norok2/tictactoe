import random
import board

TURNS = 1, 2


def ask_computer_move_random(board_, turn):
    avail_moves = board.avail_moves(board_)
    row, col = random.choice(avail_moves)
    board_ = board.do_move(board_, row, col, turn)
    return board_


def ask_human_move(board_, turn):
    is_valid_input = False
    while not is_valid_input:
        row = int(input('Row: '))
        col = int(input('Col: '))
        print()
        is_valid_input = board.is_valid_move(board_, row, col) \
                         and board.is_avail_move(board_, row, col)
    board_ = board.do_move(board_, row, col, turn)
    return board_


def main():
    board_ = board.make_board(3, 3)

    i = 0
    curr_turn = TURNS[i % 2]
    while not board.is_full(board_) and \
            not board.is_winner(board_, curr_turn):
        curr_turn = TURNS[i % 2]
        if curr_turn == TURNS[0]:
            board_ = ask_human_move(board_, curr_turn)
        else:  # curr_turn == TURNS[1]
            board_ = ask_computer_move_random(board_, curr_turn)
        print(board_)
        i += 1


main()
