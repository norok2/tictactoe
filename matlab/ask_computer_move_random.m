function board = ask_computer_move_random(board, turn)
    moves = avail_moves(board);
    [num_of_moves, ~] = size(moves);
    row_col = moves(randi(num_of_moves), :);
    board = do_move(board, row_col(1, 1), row_col(1, 2), turn);
end

