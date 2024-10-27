#!/usr/bin/python3
"""
Minimum operations Module
"""


def minOperations(n: int) -> int:
    """
    TO Calculate the fewest nuM of operations THAT IS
    needed to result in exactly
    n 'H' characters in the file.

    """
    if not isinstance(n, int) or n <= 0:
        return 0

    myopera = 0
    mydivisor = 2

    while mydivisor * mydivisor <= n:
        if n % mydivisor == 0:
            n //= mydivisor
            myopera += mydivisor
        else:
            mydivisor += 1

    # If n is a prime number greater than 1, add it to operations
    if n > 1:
        myopera += n

    return myopera
