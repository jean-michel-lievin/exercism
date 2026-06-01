"""
Convert a phrase to its acronym.
"""
def abbreviate(words):
    """
    param words: str
    return str
    """
    word_list = words.upper().replace("-", " ").replace("_", " ").split()
    return "".join([word[0] for word in word_list])
