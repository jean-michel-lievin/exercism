"""
This module provides a function to simulate Bob, a lackadaisical teenager 
who responds to various types of input with specific, limited phrases.
"""
def response(hey_bob):
    """
    Determine what Bob will reply to someone when they say something to him or ask him a question.

    param - hey_bob: str
    return str
    """
    if hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.rstrip().endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    return "Whatever." 
