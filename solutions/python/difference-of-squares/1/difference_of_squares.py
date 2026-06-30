"""
Find the difference between the square of the sum 
and the sum of the squares of the first N natural numbers.
"""
def square_of_sum(number):
    """
    Arg:
     - number: int
    Return int 
    """
    return sum(n for n in range(number + 1))**2
       

def sum_of_squares(number):
    """
    Arg:
     - number: int
    Return int 
    """
    return sum(n**2 for n in range(number + 1))


def difference_of_squares(number):
    """
    Arg:
     - number: int
    Return int 
    """
    return square_of_sum(number) - sum_of_squares(number)
