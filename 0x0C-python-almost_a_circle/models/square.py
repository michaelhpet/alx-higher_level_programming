#!/usr/bin/python3
"""Square class module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Blueprint for square objects.

    Attributes:
        size (int): Size of square
        x (int): X coordinate of square
        y (int): Y coordinate of square
        id (int): Unique id of square instance
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object.

        Args:
            size (int): Size of square
            x (int): X coordinate of square
            x (int): Y coordinate of square
            id (int): Unique id of square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Get informatal string representation of Square object."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
