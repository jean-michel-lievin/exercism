"""
Given an input text output it transposed.
"""
from itertools import zip_longest

def transpose(text):
    """
    Rows become columns and columns become rows.
    param str text
    return str
    """
    if text == "":
        return ""

    rows = text.split("\n")

    result = [
        "".join(col)
        for col in zip_longest(*rows, fillvalue=" ")
    ]

    # Retirer seulement les espaces qui ne sont suivis
    # d'aucun caractère dans les lignes suivantes
    for i in range(len(result)):
        line = list(result[i])

        j = len(line) - 1
        while j >= 0 and line[j] == " ":
            if any(len(result[k]) > j and result[k][j] != " "
                   for k in range(i + 1, len(result))):
                break
            j -= 1

        result[i] = "".join(line[:j + 1])

    return "\n".join(result)

    
    
 