"""
Given a string representing a matrix of numbers, return the rows and columns of that matrix.
"""
class Matrix:
    def __init__(self, matrix_string):
        self.rows = [
            list(map(int, line.split()))
            for line in matrix_string.splitlines()
        ]
        self.columns = [list(col) for col in zip(*self.rows)]
            
    def row(self, index):
        """
        Arg:
          - index: int
        Return:
          - array
        """
        return self.rows[index-1]

    def column(self, index):
        """
        Arg:
          - index: int
        Return:
          - array
        """
        return self.columns[index-1]
