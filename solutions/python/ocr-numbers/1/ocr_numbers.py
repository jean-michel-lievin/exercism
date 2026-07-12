"""
Given a grid of characters representing some digits, 
convert the grid to a string of digits. 
If the grid has multiple rows of cells, 
the rows should be separated in the output with a ",".
"""

DIGITS = [
        [" _ ", "| |", "|_|", "   "],
        ["   ", "  |", "  |", "   "],
        [" _ ", " _|", "|_ ", "   "],
        [" _ ", " _|", " _|", "   "],
        ["   ", "|_|", "  |", "   "],
        [" _ ", "|_ ", " _|", "   "],
        [" _ ", "|_ ", "|_|", "   "],
        [" _ ", "  |", "  |", "   "],
        [" _ ", "|_|", "|_|", "   "],
        [" _ ", "|_|", " _|", "   "],
    ]

def convert(input_grid):
    """
    Args: 
        input_grid: array
    Return:
        digit: str
    """
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    size = sum(len(input) for input in input_grid)    
    if size % 3:
        raise ValueError("Number of input columns is not a multiple of three")

    nb_split = len(input_grid[0]) // 3
    res = []

    for r in range(0, len(input_grid), 4):
        sub_grid = input_grid[r:r+4]
        line = ""
    
        for i in range(nb_split):
            start = i * 3
            end = start + 3
            current_digit = []
            for j in range(4):
                current_digit.append(sub_grid[j][start:end])
                
            if current_digit in DIGITS:
                line += str(DIGITS.index(current_digit))
            else:
                line += "?"
        res.append(line)
    return ",".join(res)
  
    
