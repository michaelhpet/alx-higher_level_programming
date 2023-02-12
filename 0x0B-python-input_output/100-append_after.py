#!/usr/bin/python3
"""Working with input/output in Python"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line
        containing a specific string
    Args:
        filename (str): name of file to parse
        search_string (str): string to append after
        new_string (str): string to append
    """
    with open(filename, "r+", encoding="utf-8") as file:
        to_write = ""
        for line in file:
            to_write += line
            if search_string in line:
                to_write += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(to_write)
