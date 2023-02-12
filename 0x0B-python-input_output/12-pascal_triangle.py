#!/usr/bin/python3
"""Trying pascal triangle in Python"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n
    Args:
        n (int): triangle size
    """
    if n <= 0:
        return []

    p_triangle = [[1]]
    while len(triangle) != n:
        prev_row = p_triangle[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        p_triangle.append(new_row)

    return p_triangle

