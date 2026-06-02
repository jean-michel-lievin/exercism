def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    res = number
    count = 0

    while res != 1:
        if res % 2 == 0:
            res //= 2
        else:
            res = res * 3 + 1
        count += 1
    
    return count