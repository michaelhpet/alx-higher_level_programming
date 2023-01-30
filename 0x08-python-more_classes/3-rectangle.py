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

    def __str__(self):
        """Informal string representation of rectangle
        Returns:
            str: string drawing of rectangle
        """
        if self.width == 0 or self.height == 0:
            return "\n".join(["#" * self.width for _ in self.height])
        return join()

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

    def area(self):
        """Computes the area of this rectangle
        Returns:
            int: self.width * self.height
        """
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of this rectangle
        If width or height is zero, the perimeter is zero

        Returns:
            int: (2 * self.width) + (2 * self.height)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
