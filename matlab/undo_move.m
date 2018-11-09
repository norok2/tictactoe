function board = undo_move(board, row, col)
    if is_valid_move(board, row, col) && ~is_avail_move(board, row, col)
        board(row, col) = 0;
    else
        disp('Invalid move');
    end
end 


