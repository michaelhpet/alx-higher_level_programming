#!/usr/bin/python3
"""Has a function to check object instance"""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance of,
    or if the object is an instance of a classes that
    inherited from the specified class
    Args:
        obj (object): an instance of any class
        a_class (object): a class
    Returns:
        bool: True if obj is instance of a_class, False otherwise
    """
    return isinstance(obj, a_class)
