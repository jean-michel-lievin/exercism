def factors(value):
    res = []
    divider = 2
    while value > 1:
        while value % divider == 0:
            res.append(divider)
            value //= divider
        divider += 1    
    return res    
