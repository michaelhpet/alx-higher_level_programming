#!/usr/bin/python3
"""Working with Python inheritance"""


class MyInt(int):
    """Defines MyInt object"""
    def __eq__(self, other):
        return self != other

    def __ne__(self, other):
        return self == other
