"""
Write a Roman numeral we use the following Latin letters
M 	  D 	C 	  L    X 	V 	I
1000  500 	100   50   10 	5 	1
"""

romans = {
    "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, 
    "XL": 40, "L": 50, "XC": 90, "C": 100, 
    "CD": 400, "D": 500, "CM": 900, "M": 1000
}

def roman(number):
    """
    param number : int
    return str
    """
    res = ""
    # We begin with the highest values
    for rom, alg in reversed(romans.items()):
        # We count how many times alg in number
        count = number // alg
        res += count * rom
        number %= alg
        
    return res
