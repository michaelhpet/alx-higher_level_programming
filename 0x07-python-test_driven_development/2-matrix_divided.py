#!/usr/bin/python3
"""Arithmetic division operation with matrices"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    Args:
        matrix (list): list of lists of equal length
        div (int, float): divisor
    Returns:
        list: a new_matrix of divided matrix elements
    Raises:
        TypeError:
            - matrix must be a matrix (list of lists) of integers/floats
            - Each row of the matrix must have the same size
            - div must be a number
    Description:
        All elements of the matrix are divided by ``div`` and rounded to
        2 decimal places
    """
    if (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(x, (int, float)) for row in matrix for x in row)
    ):
        raise TypeError('matrix must be a matrix (list of lists) of'
                        ' integers/floats')

    size = len(matrix[0])
    if not all(len(row) == size for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(element / div, 2) for element in row])

    return new_matrix
