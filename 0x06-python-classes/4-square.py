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
        self.size = size

    @property
    def size(self):
        """Gets the size attribute of a Square object
        Returns:
            int: attribute size of self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute of a Square object
        Args:
            value (int): value to set for size attribute
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Computes the area of a Square object
        Returns:
            int: area of self
        """
        return self.__size ** 2
