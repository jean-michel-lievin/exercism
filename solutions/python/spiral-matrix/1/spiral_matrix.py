"""
Return a square matrix of a given size.
The matrix should be filled with natural numbers, 
starting from 1 in the top-left corner, 
increasing in an inward, clockwise spiral order
"""
def spiral_matrix(size):
    """
    Arg:
      size (int): dimension of matrix
    Return:
        list[list[int]]: The generated spiral matrix
    """
    if size <= 0:
        return []
    res = [[0]* size for _ in range(size)]
    count = 1
    d = 0
    directions = [
        (0, 1), # right
        (1, 0), # bottom
        (0, -1), #left
        (-1, 0), # top
    ]
    line, col = 0, 0 # start point
    res[line][col] = 1
    while count < size * size:
        dline, dcol = directions[d] # tuple position
        next_line = dline + line
        next_col = dcol + col
        if next_line < 0 or next_line >= size or \
           next_col < 0 or next_col >= size or res[next_line][next_col] != 0:
            d = (d + 1) % 4
            continue

        line, col = next_line, next_col #movement   
        count += 1
        res[line][col] = count
    
    return res
