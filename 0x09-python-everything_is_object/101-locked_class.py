#!/usr/bin/python3
"""Demonstration: locking a class"""


class LockedClass:
    """Prevents user from dynamically creating new
    instance attributes, except if the instance attribute
    is called ``first_name``
    """
    def __setattr__(self, name, value):
        """Controls dynamic attribute assignments"""
        if name != "first_name":
            raise AttributeError('object has no attribute {:s}'.format(value))
        super().__setattr__(self, name, value)
