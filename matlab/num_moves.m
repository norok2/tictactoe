function result = num_moves(board)
    is_cell_empty = board ~= 0;
    result = sum(is_cell_empty(:));
end
