#!/usr/bin/python3
"""Module for working with matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices
    Args:
        m_a (list): list of lists of integers or floats
        m_b (list): list of lists of integers or floats
    Returns:
        list: new matrix which elements are products of
            m_a and m_b
    Raises:
        TypeError:
            - m_a must be a list
            - m_b must be a list
            - m_a must be a list of lists
            - m_b must be a list of lists
            - m_a should contain only integers or floats
            - m_b should contain only integers or floats
            - each row of m_a must be of the same size
            - each row of m_b must be of the same size
        ValueError:
            - m_a can't be empty
            - m_b can't be empty
            - m_a and m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError('m_b should contain only integers or floats')

    m_a_cols = len(m_a[0])
    if not all(len(row) == m_a_cols for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    m_b_cols = len(m_b[0])
    if not all(len(row) == m_b_cols for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    m_a_rows = len(m_a)
    m_b_rows = len(m_b)
    if m_a_cols != m_b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    m_product = []
    for row in m_a:
        m_product_row = []
        for index in range(m_b_cols):
            m_b_reversed = reverse_matrix(m_b)
            m_product_row_element = 0
            for x, y in zip(row, m_b_reversed[index]):
                m_product_row_element += x * y
            m_product_row.append(m_product_row_element)
        m_product.append(m_product_row)

    return m_product

def reverse_matrix(matrix):
    """Reverses a matrix
    Args:
        matrix (list): matrix to reverse
    Returns:
        list: a new reversed matrix
    """
    matrix_reversed = []
    for index in range(len(matrix)):
        row_reversed = []
        for row in matrix:
            row_reversed.append(row[index])
        matrix_reversed.append(row_reversed)

    return matrix_reversed
