#!/usr/bin/python3
"""Working with Python inheritance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square object"""

    def __init__(self, size):
        """Initializes a Square object"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the Square instance
        Returns:
            int: area of instance
        """
        return self.__size ** 2
