#!/usr/bin/python3
"""Demonstration of Python classes
"""


class Square:
    """Defines a Square
    Attributes:
        size (int): size of the Square
        position (tuple): position of the Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance
        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size attribute of a Square instance
        Returns:
            int: attribute size of self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute of a Square instance
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

    @property
    def position(self):
        """Gets the position attribute of a Square instance
        Returns:
            tuple: position of self
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute of a Square instance
        Args:
            value (tuple): value for position attribute of self
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(i, int) for i in value) and
                all(i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Computes the area of a Square instance
        Returns:
            int: area of self
        """
        return self.__size ** 2

    def my_print(self):
        """prints self with the character # to stdout
        Prints an empty line is self.size is 0
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for j in range(self.size):
            print(self.position[0] * " " + "#" * self.size)
