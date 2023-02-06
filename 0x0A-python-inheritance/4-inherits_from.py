#!/usr/bin/python3
"""Has a function to check object instance"""


def inherits_from(obj, a_class):
    """Returns true if an object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class, otherwise False
    Args:
        obj (object): an instance of any class
        a_class (object): a class
    Returns:
        bool: True if obj is instance of a_class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
