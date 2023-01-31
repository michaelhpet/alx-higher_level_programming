#!/usr/bin/python3
"""Module solely for function print_square"""


def print_square(size):
    """Prints a square with character #
    Args:
        size (int): size of square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    print("\n".join(["#" * size for _ in range(size)]))
