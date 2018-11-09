TURNS = [1, 2];

board = make_board(3, 3);


i = 0;
while ~is_full(board)
    curr_turn = TURNS(mod(i, 2) + 1);
    if curr_turn == TURNS(1)
        board = ask_human_move(board, curr_turn);
    else  % curr_turn == TURNS(2)
        board = ask_computer_move_random(board, curr_turn);
    end
    i = i + 1;
    board
end