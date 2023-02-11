#!/usr/bin/python3
"""Working with input/output in Python"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (utf-8)
    Args:
        filename (str): name of file to write to
        text (str): string to write into file
    Returns:
        int: total number of characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
