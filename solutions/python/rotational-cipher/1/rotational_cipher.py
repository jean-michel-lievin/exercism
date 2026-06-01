from string import ascii_lowercase, ascii_uppercase
# import re

def rotate(text, key):
    # letters = ascii_lowercase
    # new_letters = letters[key:] + letters[:key]
    # res = ""
    # for i in text:
    #     if re.search(r"[^a-zA-Z]", i):
    #         res += i
    #     else:    
    #         is_upper = i.isupper()
    #         lower = i.lower()
    #         new_letter = new_letters[letters.index(lower)]
    #         res += new_letter.upper() if is_upper else new_letter
        
    # return res    
    key = key % 26  # key=26 → 0, key=27 → 1
    lower_map = str.maketrans(ascii_lowercase, ascii_lowercase[key:] + ascii_lowercase[:key])
    upper_map = str.maketrans(ascii_uppercase, ascii_uppercase[key:] + ascii_uppercase[:key])
    
    return text.translate(lower_map).translate(upper_map)
