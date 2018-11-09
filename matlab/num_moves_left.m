function result = num_moves_left(board)
    is_cell_empty = board == 0;
    result = sum(is_cell_empty(:));
end
