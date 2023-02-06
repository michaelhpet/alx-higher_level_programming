#!/usr/bin/python3
"""Working with Python inheritance"""


class BaseGeometry:
    """Defines a base geometry object"""
    def area(self):
        """Raises an Exception that area is not implemented
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value
        Raises:
            TypeError: <name> must be an in integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
