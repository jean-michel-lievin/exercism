"""
Code that can verify that brackets, braces, and parentheses are balanced before attempting to run it on the Bracketeer
"""

PAIRS = {"}":"{", ")":"(", "]":"["}

def is_paired(input_string):
    """
    param input_string : str
    return bool
    """
    stack = []
    for char in input_string:
        if char in "{([":
            stack.append(char)
        elif char in "})]":
            # If the stackis empty or if the last opening is wrong
            if not stack or stack.pop() != PAIRS[char]:
                return False
    # If the stack is empty, all is well closed  
    return not stack         