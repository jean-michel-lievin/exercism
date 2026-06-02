"""
Given a target word and one or more candidate words, your task is to find the candidates that are anagrams of the target.
"""
def find_anagrams(word, candidates):
    """
    param word: str
    param candidates: [str]
    return [str]
    """
    return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted(word.lower()) and word.lower() != candidate.lower()]
