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

    @property
    def size(self):
        """Get/Set size attribute of Square object."""
        return self.width

    @size.setter
    def size(self, value):
        """Get/Get size attribute of Square object."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update dimensions and coordinates.

        Args:
            *args (int[]): list of update values
                - id (int): New unique id attribute
                - size (int): New size of Square object
                - x (int): New x coordinate of Square object
                - y (int): New y coordinate of Square object
            **kwargs (Dict<str, int>): keyworded arguments of update values
        """
        attributes = ["id", "size", "x", "y"]
        for entry in enumerate(args):
            setattr(self, attributes[entry[0]], entry[1])

        if len(args) == 0:
            for entry in kwargs.items():
                setattr(self, entry[0], entry[1])

    def __str__(self):
        """Get informatal string representation of Square object."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
