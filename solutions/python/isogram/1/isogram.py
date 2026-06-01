"""
Determine if a word or phrase is an isogram.
"""
import re

def is_isogram(string):
    """
    param str string
    return bool
    """
    #return sorted(Counter(re.sub(r"[-\s]+", "", string.lower())).values())[-1] == 1 if string != "" else True
    cleaned = re.sub(r"[^a-z]", "", string.lower())
    return len(cleaned) == len(set(cleaned))