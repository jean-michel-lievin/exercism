"""
Calculate the Hamming distance between two DNA strands.
"""
def distance(strand_a, strand_b):
    """
    Args: 
     - strand_a: str
     - strand_b: str
    Return:
     - int
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(a != b for a, b in zip(strand_a, strand_b))