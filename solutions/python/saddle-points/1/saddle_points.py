"""
Find the potential trees where you could build your tree house.
"""


def saddle_points(matrix):
    """
    Args:
    matrix: [int]
    Return:
    res: [int]
    """
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    res = []
    columns = list(zip(*matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current = matrix[i][j]
            is_max_row = current == max(matrix[i])
            is_min_col = current == min(columns[j])
            if is_min_col and is_max_row:
                res.append({"row": i + 1, "column": j + 1})
    return res
