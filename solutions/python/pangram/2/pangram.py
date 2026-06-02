"""
 figure out if a sentence is a pangram.
"""
import re

def is_pangram(sentence):
    """
    param: sentence str
    retrun bool
    """
    return "".join(sorted(set(re.sub(r"[^a-z]", "", sentence.lower())))) == "abcdefghijklmnopqrstuvwxyz"