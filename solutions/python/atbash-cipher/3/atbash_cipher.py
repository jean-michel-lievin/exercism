"""
Create an implementation of the Atbash cipher, 
an ancient encryption system created in the Middle East.
"""
from string import ascii_lowercase

TRANS_TABLE = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(plain_text):
    """
    param plain_text : str
    retrun str
    """
    cleaned = "".join(text.translate(TRANS_TABLE) for text in plain_text.lower() if text.isalnum())
    return " ".join(cleaned[idx:idx+5] for idx in range(0, len(cleaned), 5))
    

def decode(ciphered_text):
    """
    param ciphered_text : str
    retrun str
    """
    return "".join(text.translate(TRANS_TABLE) for text in ciphered_text if text.isalnum())
