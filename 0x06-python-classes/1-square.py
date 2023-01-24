#!/usr/bin/python3
"""Class with a private instance attribute

This module demonstrates the creation of class
with a private instance attribute in Python
"""
class Square:
    """Defines a Square

    Attributes:
        size (int): size of the Square
    """
    def __init__(self, size):
        """Initializes a Square object
        
        Args:
            size (int): size of square
        """
        self.__size = size
