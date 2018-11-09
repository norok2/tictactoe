function result = is_valid_move(board, row, col)
    [max_row, max_col] = size(board);
    result = row >= 1 && row <= max_row && col >= 1 && col <= max_col; 
end

