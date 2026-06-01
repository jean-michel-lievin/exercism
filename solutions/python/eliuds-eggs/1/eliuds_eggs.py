"""
Your task is to count the number of 1 bits in the binary representation of a number.
"""
def egg_count(display_value):
    """
    Defend to use bit_count()
    param display_value: str
    return int
    """
    res = 0
    while display_value > 0:
        display_value = display_value & (display_value - 1)
        res += 1
    return res

    
    # Pas opti
    # res = 0
    # while display_value > 0:
    #     if display_value % 2 == 1:
    #         res += 1
    #         display_value = divmod(display_value, 2)[1] 
    #     else:
    #         display_value = divmod(display_value, 2)[0] 
    # return res
