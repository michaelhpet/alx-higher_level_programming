#!/usr/bin/python3
"""Working with input/output in Python"""


def write_file(filename="", text=""):
    """Writes a string to a text file (utf-8)
    Args:
        filename (str): name of file to write to
        text (str): string to write into file
    Returns:
        int: total number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text, filename)
