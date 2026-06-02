"""
Create a program that implements the Sieve of Eratosthenes algorithm 
to find all prime numbers less than or equal to a given number.
"""
from math import isqrt


def primes(limit):
    """
    Args:
    limit [int] : Array on integer
    Return:
    Array on integer
    """
    if limit < 2:
        return []

    # On suppose au départ que tous les nombres sont premiers
    is_prime = [True] * (limit + 1)
    # 0 et 1 ne sont pas premiers
    is_prime[0] = is_prime[1] = False
    # On n'a besoin de traiter que jusqu'à sqrt(n)
    n = isqrt(limit)

    for i in range(2, n + 1):
        # Si i est encore marqué comme premier
        if is_prime[i]:
            # Tous les multiples de i à partir de i*i ne sont pas premiers
            for mutiple in range(i * i, limit + 1, i):
                is_prime[mutiple] = False


    # On reconstruit la liste des nombres premiers
    return [i for i, is_prime in enumerate(is_prime) if is_prime]
 
            