#!/usr/bin/python3
"""
Python inheritance
"""


class MyList(list):
    """
    Subclass of list
    """

    def __init__(self):
        """Initialized a MyList instance"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
