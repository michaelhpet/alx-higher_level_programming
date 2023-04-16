#!/usr/bin/python3
"""Rectangle class module."""
from models.base import Base


class Rectangle(Base):
    """Blueprint for rectangle objects.

    Attributes:
        width (int): Width of rectangle
        height (int): Height of rectangle
        x (int): X coordinate of rectangle
        y (int): Y coordinate of rectangle
        id (int): Unique id of rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle.

        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
            x (int): X coordinate of rectangle
            y (int): Y coordinate of rectangle
            id (int): Unique id of rectangle

        Raises:
            TypeError: width, height, x, and y must be int
            ValueError: width and height must be > 0
            ValueError: x and y must be >= 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/Set the width attribute of rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        """Get/Set the width attribute of rectangle object."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height attribute of rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get/Set the height attribute of rectangle object."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/Set the x attribute of rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        """Get/Set the x attribute of rectangle object."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/Set the y attribute of rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        """Get/Set the y attribute of rectangle object."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the Rectangle instance.

        Returns:
            int: Area of Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """Print Rectangle instance.

        Prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Update dimensions and coordinates.

        Args:
            *args (int[]): list of update values
                - id (int): New unique id attribute
                - width (int): New width of rectangle
                - height (int): New height of rectangle
                - x (int): New x coordinate of rectangle
                - y (int): New y coordinate of rectangle
            **kwargs (Dict<str, int>): keyworded arguments of update values
        """
        attributes = ["id", "width", "height", "x", "y"]
        for entry in enumerate(args):
            setattr(self, attributes[entry[0]], entry[1])

        if len(args) == 0:
            for entry in kwargs.items():
                setattr(self, entry[0], entry[1])

    def to_dictionary(self):
        """Get the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Get informal string representation of Rectangle object."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)
