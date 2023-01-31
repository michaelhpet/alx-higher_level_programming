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

    m_a_size = len(m_a[0])
    if not all(len(row) == m_a_size for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    m_b_size = len(m_b[0])
    if not all(len(row) == m_b_size for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a) != m_b_size:
        raise ValueError("m_a and m_b can't be multiplied")

    m_a_reversed = []
    for index in range(len(m_a)):
        row_reversed = []
        for row in m_a:
            row_reversed.append(row[index])
        m_a_reversed.append(row_reversed)

    m_product = []
    for index in range(len(m_a_reversed)):
        row_product = []
        for x, y in zip(m_a_reversed[index], m_b[index]):
            row_product.append(x * y)
        m_product.append(row_product)

    return m_product
