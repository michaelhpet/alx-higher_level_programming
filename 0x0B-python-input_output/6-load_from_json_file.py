#!/usr/bin/python3
"""Working with input/output in Python"""


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        filename (str): name of file to load from
    Returns:
        object: object loaded from file
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
