"""
Determine the RNA complement of a given DNA sequence.
"""
def to_rna(dna_strand):
    """
    Determine the RNA complement of a given DNA sequence.
    param dna_strnad : str
    """
    dna_rna = {"G":"C", "C":"G", "T":"A", "A": "U"}
    return "".join(dna_rna.get(str, "") for str in dna_strand) 
