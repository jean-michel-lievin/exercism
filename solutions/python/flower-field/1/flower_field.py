def annotate(garden):
    """
    Arg:
      - garden: matrix of flowers
    """
    if garden == []:
        return []

    rows = len(garden)
    cols = len(garden[0])
    res = [list(row) for row in garden]

    for row in range(rows):
        if len(garden[row]) != cols:
            raise ValueError("The board is invalid with current input.")
        for col in range(cols):
            if garden[row][col] not in [" ", "*"]:
                raise ValueError("The board is invalid with current input.")
            if garden[row][col] == "*":
                continue


            count = 0
            for delta_row in [-1, 0, 1]:
                for delta_col in [-1, 0, 1]:
                    new_row, new_col = row + delta_row, col + delta_col
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if garden[new_row][new_col] == "*":
                            count += 1
            if count > 0:
                res[row][col] = str(count)

    return ["".join(row) for row in res]
