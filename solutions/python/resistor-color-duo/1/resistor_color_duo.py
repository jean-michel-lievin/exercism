"""
The program will take color names as input and output a two digit number, 
even if the input is more than two colors!
"""
RESISTORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def value(colors):
    """
    param colors : str
    return int
    """
    return int("".join(str(RESISTORS.index(color)) for color in colors[:2]))
