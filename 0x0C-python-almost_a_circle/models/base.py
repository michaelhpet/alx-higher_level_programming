#!/usr/bin/python3
"""Base class module."""
import json


class Base:
    """Base blueprint for project-wide objects.

    The goal of this class is to manage the id attribute
    of objects create from this classes and subclasses
    therefore preventing the duplication of code and logic.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object.

        Args:
            id (int): Unique id number of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Get JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of objects to file.

        Args:
            list_objs (list): List of objects
        """
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open("{:s}.json".format(cls.__name__), "w") as file:
            file.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Get list of objects from JSON string.

        Args:
            json_string (str): String to parse
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set.

        Args:
            dictionary (Dict<str, int>): Dictionary or keyworded arguments
            to parse
        """
        dummy_obj = cls(10, 10, 10)
        dummy_obj.update(**dictionary)
        return dummy_obj
