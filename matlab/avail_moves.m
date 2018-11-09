function result = avail_moves(board)
    [rows, cols] = find(board == 0);
    result = [rows cols];
end

