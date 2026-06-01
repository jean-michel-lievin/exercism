"""
Given a name and a number, 
your task is to produce a sentence using 
that name and that number as an ordinal numeral
"""
def line_up(name, number):
    """
    param: name (str)
    param: number (int)
    return str
    """
    num = str(number)

    if num.endswith(("11", "12", "13")):
        suffix = "th"
    else:
        suffix = {"1": "st", "2": "nd", "3": "rd"}.get(num[-1], "th")
    
    return f"{name}, you are the {num}{suffix} customer we serve today. Thank you!"
    