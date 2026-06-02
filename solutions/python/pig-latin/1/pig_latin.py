"""
Translate text from English to Pig Latin.
"""
def translate(text):
    """
    Translate text from English to Pig Latin.
    
    param - text: str
    return str
    """
    vowels = "aeiou"
    pattern = "ay"
    words = text.split()
    pos = 0
    result = []
    for word in words:
        if word[0] in vowels or word.startswith(("xr", "yt")):
            return text + pattern
        for idx, letter in enumerate(word):
            if letter == "u" and idx > 0 and word[idx-1] == "q":
                pos = idx + 1 
                break
            if letter == "y" and idx > 0 and word[idx-1] not in vowels:
                pos = idx
                break
            if letter in vowels:
                pos = idx
                break
            
        result.append(word[pos:] + word[:pos] + pattern)    
    return " ".join(result)       
            