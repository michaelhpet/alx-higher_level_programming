#!/usr/bin/python
"""Integer addition"""


def add_integer(a, b=98):
    """adds two integers
    Args:
        a (int, float): first number to add
        b (int, float): second number to add
    Raises:
        TypeError: a and b must be integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
