"""
 figure out if a sentence is a pangram.
"""
import re
import string

def is_pangram(sentence):
    """
    param: sentence str
    retrun bool
    """
    return "".join(sorted(set(re.sub(r"[^a-z]", "", sentence.lower())))) == "abcdefghijklmnopqrstuvwxyz"