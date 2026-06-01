"""
Compute a word's Scrabble score by summing the values of its letters.
"""

SCORES = {
    1: "AEIOULNRST", 
    2: "DG", 
    3: "BCMP",
    4: "FHVWY", 
    5: "K", 
    8: "JX", 
    10: "QZ"}

# Inversed dictionnary to have a one-to-oen relationship
LETTER_SCORE = {
    letter: score
    for score, letters in SCORES.items()
    for letter in letters  
}

def score(word):
    """
    param:  word (str)
    return int
    """
    return sum(LETTER_SCORE.get(letter, 0) for letter in word.upper())