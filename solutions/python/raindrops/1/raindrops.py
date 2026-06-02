"""
Your task is to convert a number into its corresponding raindrop sounds.
"""
def convert(number):
    """
    param: number - str
    """
    # if number % 3 and number % 5 and number % 7:
    #     return str(number)
    # res = ""    
    # if number % 3 == 0:
    #     res += "Pling"
    # if number % 5 == 0:
    #     res += "Plang"
    # if number % 7 == 0:
    #     res += "Plong"
    drops = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

    res = "".join(drop for val, drop in drops if number % val == 0)
    
    return res or str(number)