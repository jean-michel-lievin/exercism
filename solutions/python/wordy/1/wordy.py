"""
Parse and evaluate simple math word problems returning the answer as an integer.
"""

def answer(question):
    """
    param question : str
    return int
    """
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    
    s = question.replace("What is", "").replace("?", "").replace("by", "").strip()
    tokens = s.split()
    
    if not tokens:
        raise ValueError("syntax error")

    try:
        res = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")

    i = 1
    while i < len(tokens):
        op = tokens[i]

        if i + 1 >= len(tokens):
            if op not in ["plus", "minus", "multiplied", "divided"]:
                raise ValueError("unknown operation")
            else:    
                raise ValueError("syntax error")
        if tokens[-1].isdigit() and tokens[-2].isdigit():
            raise ValueError("syntax error")
            
        try:
            next_val = int(tokens[i+1])
        except ValueError:
            raise ValueError("syntax error")

        if op == "plus":
            res += next_val
        elif op == "minus":
            res -= next_val
        elif op == "multiplied":
            res *= next_val
        elif op == "divided":
            res = int(res / next_val)
            
        i += 2
        
    return res