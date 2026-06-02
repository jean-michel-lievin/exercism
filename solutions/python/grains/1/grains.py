"""
Calculate the number of grains of wheat on a chessboard.
"""
def square(number):
    """
    the number of grains on a given square
    """
    if number not in range(1, 65):
       raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)

def total():
    """
    the total number of grains on the chessboard
    """
    return sum(square(i) for i in range(1, 65))    
