"""
This exercise is about translating the colors into a label
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


def label(colors):
    """
    param colors : array
    return string
    """
    val = "".join(str(RESISTORS.index(color)) for color in colors[:2])
    nb_zero = int(RESISTORS.index(colors[2]))
    total_ohms = int(val) * (10** nb_zero)

    if total_ohms > 1_000_000_000:
        return f"{total_ohms // 1_000_000_000} gigaohms"
    if total_ohms >= 1_000_000:
        return f"{total_ohms // 1_000_000} megaohms"
    if total_ohms >= 1_000:
        return f"{total_ohms // 1_000} kiloohms"
    return f"{total_ohms} ohms"    
        
    
    
    
        
        
