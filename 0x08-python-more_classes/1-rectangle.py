#!/usr/bin/python3
"""Module solely for a Rectangle class"""


class Rectangle:
    """A class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        Raises:
            TypeError:
                - width must be an integer
                - height must be an integer
            ValueError:
                - width must be >= 0
                - height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
