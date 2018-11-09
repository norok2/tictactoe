function result = is_empty(board)
    % : alternate implementation
    % result = num_moves(board) == 0;
    result = sum(board(:)) == 0;
end
