#!/usr/bin/python3
"""Working with input/output in Python"""


class Student:
    """Defines a student
    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance
        """
        to_retrieve = self.__dict__
        if attrs is not None:
            f = lambda item: item[0] in attrs
            to_retrieve = dict(filter(f, to_retrieve.items()))
        return to_retrieve
