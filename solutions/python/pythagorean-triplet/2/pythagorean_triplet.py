"""
Given an input integer N, 
find all Pythagorean triplets for which a + b + c = N.

Instructions:
-------------
a² + b² = c²
a < b < c
c=N−a−b
b=(N²−2Na) / (2N - 2a)
"""
def triplets_with_sum(number):
    """
    Args:
    number: int
    Return:
    res : [int, int, int] Array with the three values
    """
    res = []

    for a in range(1, number // 3):
        nominator = number**2 - 2*number*a
        denominator = 2*number - 2*a
        if nominator % denominator == 0:
            b = nominator // denominator
            if b > a:
                c = number - a - b
                res.append([a, b, c])



    return res
