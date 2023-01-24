#!/usr/bin/python3
"""Demonstration of Python classes"""


class Square:
    """Defines a Square
    Attributes:
        size (int): size of the Square
    """
    def __init__(self, size=0):
        """Initializes a Square object
        Args:
            size (int): size of square
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size attribute of a Square object"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Computes the area of a Square object
        Returns:
            int: area of self
        """
        return self.__size ** 2

    def __gt__(self, other):
        """Binary > comparison with another instance"""
        return self.area() > other.area()

    def __lt__(self, other):
        """Binary < comparison with another instance"""
        return self.area() < other.area()

    def __ge__(self, other):
        """Binary >= comparison with another instance"""
        return self.area() >= other.area()

    def __le__(self, other):
        """Binary <= comparison with another instance"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Binary == comparison with another instance"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Binary != comparison with another instance"""
        return self.area() != other.area()
