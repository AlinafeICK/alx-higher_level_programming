#!/usr/bin/python3
"""A function def pascal_triangle(n):
that returns a list of lists of integers"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n - 1):
        row = [1]
        for j in range(len(triangle[i]) - 1):
            row.append(triangle[i][j] + triangle[i][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
