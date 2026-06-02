# [disallowed-name]
"""
Determine if a triangle is equilateral, isosceles, or scalene.
"""
def equilateral(sides):
    """
    Determine if a triangle is equilateral.

    param - sides: array[int]
    return bool
    """
    a, b, c = sides
    return a == b and b == c and a > 0


def isosceles(sides):
    """
    Determine if a triangle is isosceles.

    param - sides: array[int]
    return bool
    """
    a, b, c = sides
    
    return (a == b or b == c or a == c) and \
           (a + b >= c and b + c >= a and a + c >= b) and \
           (a > 0 and b > 0 and c > 0) 


def scalene(sides):
    """
    Determine if a triangle is scalene.

    param - sides: array[int]
    return bool
    """
    a, b, c = sides
    return (a + b >= c and b + c >= a and a + c >= b) and (a != b and b!= c and a != c)
