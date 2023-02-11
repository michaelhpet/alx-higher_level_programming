#!/usr/bin/python3
"""Working with input/output in Python"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj (object): object to serialize
    Returns:
        str: JSON representation of (or serialized) my_obj
    """
    import json
    return json.dumps(my_obj)
