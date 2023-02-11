#!/usr/bin/python3
"""Working with input/output in Python"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str (str): string to deserialize
    Returns:
        object: object represented by my_str
    """
    import json
    return json.loads(my_str)
