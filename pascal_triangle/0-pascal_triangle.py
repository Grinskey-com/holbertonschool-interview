#!/usr/bin/python3
"""defines a function that builds pascal's triangle"""


def pascal_triangle(n):
    """return pascal's triangle with n rows.

    args:
        n (int): the number of rows.

    returns:
        list: a list of lists of integers, or [] if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(n-1):
        prev = triangle[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
