"""
Count how many times each word occurs in a subtitle of a drama.
"""
from collections import Counter
import re

def count_words(sentence):
    """
    param sentence :  str
    return dict
    """

    words_split = re.sub(r"[^a-z0-9\s']", " ", sentence.lower()).split()
    
    words_list = [word.strip("'") for word in words_split if word.strip("'")]
    
    return Counter(words_list)
