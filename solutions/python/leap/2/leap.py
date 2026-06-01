"""
Determine whether a given year is a leap year.
"""
def leap_year(year):
    """
    Determine whether a given year is a leap year.
    param - year : str
    return - bool
    """
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
