#!/usr/bin/python3
"""Base class module."""
import json
import csv
import turtle
import random


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
        with open("{:s}.json".format(cls.__name__), "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
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
        if cls.__name__ == "Rectangle":
            shape = cls(10, 10)
        else:
            shape = cls(10)

        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """Create list of instances from file."""
        try:
            with open("{:s}.json".format(cls.__name__), "r") as file:
                list_dictionaries = Base.from_json_string(file.read())
                return [cls.create(**dict) for dict in list_dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of objects and save to CSV file.

        Args:
            list_objs (list): List of [inherited] instances of Base class.
        """
        with open("{:s}.csv".format(cls.__name__), "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                if len(list_dictionaries) == 0:
                    file.write("[]")
                else:
                    fieldnames_dict = {
                        "Rectangle": ["id", "width", "height", "x", "y"],
                        "Square": ["id", "size", "x", "y"]
                    }
                    fieldnames = fieldnames_dict[cls.__name__]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    for row in list_dictionaries:
                        writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Create a list of instances from deserialized CSV file."""
        try:
            with open("{:s}.csv".format(cls.__name__), "r") as file:
                fieldnames_dict = {
                    "Rectangle": ["id", "width", "height", "x", "y"],
                    "Square": ["id", "size", "x", "y"]
                }
                fieldnames = fieldnames_dict[cls.__name__]

                reader = csv.DictReader(file, fieldnames=fieldnames)
                list_dictionaries = [dict((key, int(value))
                                          for key, value in row.items())
                                     for row in reader]

                return [cls.create(**dictionary)
                        for dictionary in list_dictionaries]

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle objects to draw
            list_squares (list): List of Square objects to draw
        """
        graph = turtle.Turtle()
        graph.screen.bgcolor("#BCBCBC")
        graph.shape("circle")
        graph.color("black")
        graph.pensize(2)
        graph.speed(2)

        fillcolors = ["red", "blue", "green", "#1E1E1E", "yellow",
                      "pink", "crimson", "orange", "aqua", "darkblue"]

        for rectangle in list_rectangles + list_squares:
            graph.goto(rectangle.x, rectangle.y)
            graph.setheading(0)

            graph.showturtle()

            graph.pendown()
            graph.fillcolor(fillcolors[random.randint(0, 9)])
            graph.begin_fill()
            graph.forward(rectangle.width)
            graph.right(90)
            graph.forward(rectangle.height)
            graph.right(90)
            graph.forward(rectangle.width)
            graph.right(90)
            graph.forward(rectangle.height)
            graph.end_fill()
            graph.penup()

            graph.hideturtle()

        turtle.done()
