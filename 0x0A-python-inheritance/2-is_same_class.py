#!/usr/bin/python3
"""Has a function to check object instance"""


def is_same_class(obj, a_class):
    """Returns true if an object is exactly an instance
    of the specified class
    Args:
        obj (object): an instance of any class
        a_class (object): a class
    Returns:
        bool: True if obj is instance of a_class, False otherwise
    """
    return type(obj) == a_class
