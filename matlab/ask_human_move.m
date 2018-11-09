function board = ask_human_move(board, turn)
    is_valid_input = 0;
    while ~is_valid_input
        row = input('Input row: ');
        col = input('Input col: ');
        if is_valid_move(board, row, col) && is_avail_move(board, row, col)
            is_valid_input = 1;
        else
            is_valid_input = 0;
        end
    end
    board = do_move(board, row, col, turn);
end

