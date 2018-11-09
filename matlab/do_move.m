function board = do_move(board, row, col, turn)
    if is_valid_move(board, row, col) && is_avail_move(board, row, col)
        board(row, col) = turn;
    else
        disp('Invalid move');
    end
end

