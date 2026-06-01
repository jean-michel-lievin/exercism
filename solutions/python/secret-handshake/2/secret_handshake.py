"""
Your task is to convert a number between 1 and 31 to a sequence of actions in the secret handshake.
"""
def commands(binary_str):
    """
    param binary_str : str
    return array[str]
    """
    res = []
    # on lit le binaire de droite à gauche
    if binary_str[-1] == "1":
        res.append("wink")
    if binary_str[-2] == "1":
        res.append("double blink")
    if binary_str[-3] == "1":
        res.append("close your eyes")
    if binary_str[-4] == "1":
        res.append("jump")
    # on inverse au 5e
    if binary_str[-5] == "1":
        res.reverse()
    return res
    
