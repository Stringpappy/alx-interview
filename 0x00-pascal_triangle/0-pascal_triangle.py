#!/usr/bin/python3
"""
Pascal Triangle Generator
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for row in range(1, n):
        new_row = [1]
        for col in range(len(triangle[row - 1]) - 1):
            previous_row = triangle[row - 1]
            new_row.append(previous_row[col] + previous_row[col + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
