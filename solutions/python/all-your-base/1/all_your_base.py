"""
Convert a sequence of digits in one base, representing a number, 
into a sequence of digits in another base, 
representing the same number.
"""
def rebase(input_base, digits, output_base):
    """
    Args:
      - input base: int
      - digits: array
      - output_base: int
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    if len(digits) == 1 and digits[0] == 1:
        return digits


    value = 0
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        value = value * input_base + digit

    if value == 0:
        return [0]

    res = []

    while value > 0:
        res.append(value % output_base)
        value //= output_base
        
    return res[::-1]
