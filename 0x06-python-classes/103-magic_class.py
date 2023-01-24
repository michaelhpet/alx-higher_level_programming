#!/usr/bin/python3
"""Decoding python ByteCodes that use classes"""
import math


class MagicClass:
    """Blueprint for Magic"""
    def __init__(self, radius=0):
        """Initializes a MagicClass instance
        Args:
            radius (int, float): radius attribute of MagicClass instance
        """
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes the area of a MagicClass instance"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Computes the circumference of a MagicClass instance"""
        return 2 * math.pi * self.__radius
