#!/usr/bin/python3
"""Demonstration: locking a class"""


class LockedClass:
    """Prevents user from dynamically creating new
    instance attributes, except if the instance attribute
    is called ``first_name``
    """
    __slots__ = ['first_name']
