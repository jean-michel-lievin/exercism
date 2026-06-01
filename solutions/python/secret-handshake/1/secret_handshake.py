def commands(binary_str):
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
    
