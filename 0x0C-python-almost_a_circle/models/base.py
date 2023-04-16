#!/usr/bin/python3
"""Base class module."""


class Base:
    """Base blueprint for project-wide objects.

    The goal of this class is to manage the id attribute
    of objects create from this classes and subclasses
    therefore preventing the duplication of code and logic.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object.

        Args:
            id (int): Unique id number of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
