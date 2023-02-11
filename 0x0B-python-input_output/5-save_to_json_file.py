#!/usr/bin/python3
"""Working with input/output in Python"""


def save_to_json_file(my_obj, filename):
    """Writes an object to file using a JSON representation
    Args:
        my_obj (object): object to write
        filename (str): name of file to write to
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
