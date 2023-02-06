#!/usr/bin/python3
"""Python inheritance"""


class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
