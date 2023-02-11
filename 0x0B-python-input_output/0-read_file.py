#!/usr/bin/python3
"""Input/Output with the Python programming language"""


def read_file(filename=""):
    """Reads a text file (utf-8) and prints it to stdout
    Args:
        filename (str): name of file to read
    """
    with open(filename) as file:
        for line in file:
            print(line)
