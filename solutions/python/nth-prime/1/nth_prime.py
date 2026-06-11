"""
Given a number n, determine what the nth prime is.
"""

def prime(number):
   
    if number < 1:
        raise ValueError('there is no zeroth prime')

    gen = prime_generator()
    prime = None
    for _ in range(number):
        prime = next(gen)
    return prime

def is_prime(x):
    if x < 2:
        return False
    for p in range(2, int(x**0.5) + 1):
        if x % p == 0:
            return False
    return True
    
def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1