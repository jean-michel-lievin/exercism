"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if list_one != [] and list_two == []:
        return SUPERLIST
    if list_one == [] and list_two != []:
        return SUBLIST
    if list_one in list_two:
        return SUBLIST
    if list_two in list_one:
        return SUPERLIST
    if is_sublist(list_one, list_two):
        return SUBLIST  
    if is_sublist(list_two, list_one):
        return SUPERLIST
    if list_one != list_two:
        return UNEQUAL
        
    
def is_sublist(needle, haystack):
    n, m = len(needle), len(haystack)
    if n == 0:
        return True
    if n > m:
        return False
    return any(haystack[i:i+n] == needle for i in range(m - n + 1))    
