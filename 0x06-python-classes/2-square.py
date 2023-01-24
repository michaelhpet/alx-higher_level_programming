#!/usr/bin/python3
"""Demonstration of Python classes
"""


class Square:
    """Defines a Square

    Attributes:
        size (int): size of the Square
    """
    def __init__(self, size=0):
        """Initializes a Square object

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
