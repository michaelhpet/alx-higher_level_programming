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
