#!/usr/bin/python3
"""Working with input/output in Python"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
        structure for JSON serialization of an object
    Args:
        obj (object): object to serialize
    """
    return obj.__dict__
