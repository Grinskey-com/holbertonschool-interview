#!/usr/bin/python3
"""
Minimum operations calculation
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result
    in (n) H chars in the file.
    """
    if n <= 1:
        return 0

    ops = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1
    if n > 1:
        ops += n

    return ops
