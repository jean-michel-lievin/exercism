"""
Translate RNA sequences into proteins.
"""
RNA_SEQUENCES = {
    "AUG": "Methionine", 
    "UUU": "Phenylalanine", 
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine", 
    "UAC": "Tyrosine", 
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan", 
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}

def proteins(strand):
    """
    Args:
      - strand : str
    """
    res = []
    for code in range(0, len(strand), 3):
        seq = strand[code:code+3]
        if seq in RNA_SEQUENCES:
            if RNA_SEQUENCES[seq] == "STOP":
                return res
            res.append(RNA_SEQUENCES[seq])
    return res
