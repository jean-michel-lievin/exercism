"""
Given a string of digits, output all the contiguous substrings 
of length n in that string in the order that they appear.
"""
def slices(series, length):
    """
    Args:
        - series : str
        - length : int
    Return:
        - array
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if not series:
        raise ValueError("series cannot be empty")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    
    return [series[s:s+length] for s in range(len(series) - length + 1)]
