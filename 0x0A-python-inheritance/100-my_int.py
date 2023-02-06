#!/usr/bin/python3
"""Working with Python inheritance"""


class MyInt(int):
    """Defines MyInt object"""

    """equal-to operator"""
    def __eq__(self, other):
        return self != other

    def __ne__(self, other):
        """not-equal-to operator"""
        return self == other
