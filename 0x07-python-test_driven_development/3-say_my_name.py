#!/usr/bin/python3
"""Module solely for function say_my_name"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first_name> <last_name>
    Description: <last_name> is optional and only first
        name will be printed if it's omitted
    Args:
        first_name (str): first name string
        last_name (str): optional last name string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
