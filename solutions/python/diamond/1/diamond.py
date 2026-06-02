"""
Given a letter, it prints a diamond starting with 'A', 
with the supplied letter at the widest point.
"""
from string import ascii_uppercase


def rows(letter):
    """
    param letter: str
    return [str]
    """
    letters = ascii_uppercase[:(ascii_uppercase.index(letter)+1)]
    res = []
    width = 2 * len(letters) - 1
    for idx, letter in enumerate(letters):
        if idx == 0:
            res.append(letter.center(width, " "))
        else:
            inner_space = 2 * idx - 1 
            res.append(f"{letter}{inner_space*" "}{letter}".center(width, " ")) 
    return res  + res[:-1][::-1]