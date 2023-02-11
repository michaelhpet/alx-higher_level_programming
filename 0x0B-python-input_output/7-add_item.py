#!/usr/bin/python3
"""Working with input/output in Python"""
from sys import argv

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Adds all arguments to a Python list
    and then save them to a file
    """
    filename = "add_item.json"

    existing = []
    try:
        existing = load_from_json(filename)
    except Exception:
        pass

    arguments = argv[1:]
    to_save = existing + arguments

    with open(filename, "w", encoding="utf-8") as file:
        save_to_json(existing, filename)
