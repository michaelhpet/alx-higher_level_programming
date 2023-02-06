#!/usr/bin/python3
"""Adding attributes to objects if possible"""


def add_attribute(an_object, key, value):
    """Adds a new attribute to an object if possible
    Args:
        an_object (object): object to add attribute to
        key (string): attribute key
        value (object): attribute value
    Raises:
        TypeError: can't add new attribute (if attribute cannot be added)
    """
    if not hasattr(an_object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(an_object, key, value)
