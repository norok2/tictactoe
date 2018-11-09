function result = is_full(board)
    % : alternate implementation
    % result = num_moves_left(board) == 0;
    is_cell_empty = board == 0;
    result = sum(is_cell_empty(:)) == 0;
end

