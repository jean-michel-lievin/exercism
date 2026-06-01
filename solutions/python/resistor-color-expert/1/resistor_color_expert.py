"""
Create a helpful program so that you don't have to remember the values of the bands. The program will take 1, 4, or 5 colors as input and output the correct value in ohms. 
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

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

def resistor_label(colors):
    """
    L'interpréteur de formatage :g (pour "General format") regarde le nombre :
    - Si res = 2.0 -> il affiche "2".
    - Si res = 2.54 -> il affiche "2.54".
    param colors : array
    """

    bands_len = len(colors)
    if bands_len == 1:
        return "0 ohms"
    val = int("".join(str(RESISTORS.index(color)) for color in colors[:-2]))
    val *= 10**RESISTORS.index(colors[-2])
    tolerance = "±"+TOLERANCE.get(colors[-1])
    if val >= 1_000_000_000:
        return f"{val / 1_000_000_000:g} gigaohms {tolerance}" 
    if val >= 1_000_000:
        return f"{val / 1_000_000:g} megaohms {tolerance}"
    if val >= 1000:
        return f"{val / 1000:g} kiloohms {tolerance}"
    else:
        return str(val) + " ohms " + tolerance 
    

                  
    