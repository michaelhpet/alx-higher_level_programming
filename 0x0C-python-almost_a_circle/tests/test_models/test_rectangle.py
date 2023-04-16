#!/usr/bin/python3
"""Test module for Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys
import json
import os


class TestRectangleInstance(unittest.TestCase):
    """Unit tests for instantiation of Rectangle objects."""

    def test_rectangle_instance(self):
        """Rectangle object is an instance of Rectangle class."""
        rectangle1 = Rectangle(20, 10)
        self.assertIsInstance(rectangle1, Rectangle)

    def test_base_instance(self):
        """Rectangle object is an instance of Base class."""
        rectangle1 = Rectangle(15, 12)
        self.assertIsInstance(rectangle1, Base)

    def test_str(self):
        """Test the informal representation of Rectangle object."""
        rectangle1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rectangle1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_id(self):
        """Test for id attribute."""
        for id in [12, 56, 8, 19]:
            rectangle = Rectangle(15, 10, 8, 13, id)
            self.assertEqual(rectangle.id, id)

        rectangle1 = Rectangle(18, 11, 15, 71)
        rectangle2 = Rectangle(18, 11, 15, 71)
        rectangle3 = Rectangle(18, 11, 15, 71)
        rectangle4 = Rectangle(18, 11, 15, 71)
        rectangle5 = Rectangle(18, 11, 15, 71)

        self.assertEqual(rectangle1.id, rectangle2.id - 1)
        self.assertEqual(rectangle3.id, rectangle2.id + 1)
        self.assertEqual(rectangle1.id, rectangle5.id - 4)
        self.assertGreater(rectangle4.id, rectangle3.id)

    def test_without_dimensions(self):
        """Rectangle object initialization without width
        or height arguments.
        """
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(10)
        with self.assertRaises(TypeError):
            Rectangle(None, 3)

    def test_coordinates(self):
        """Test for coordinates attributes."""
        rectangle1 = Rectangle(15, 10)
        rectangle2 = Rectangle(18, 11, 15, 71)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.x, rectangle1.y)

        self.assertEqual(rectangle2.x, 15)
        self.assertEqual(rectangle2.y, 71)
        self.assertNotEqual(rectangle2.x, rectangle2.y)

        with self.assertRaises((ValueError, TypeError)):
            Rectangle(10, 10, -2.5, 10)

        with self.assertRaises((ValueError, TypeError)):
            Rectangle(12, 34, -0.5, -11)

    def test_wrong_types(self):
        """Rectangle object initialization with invalid width
        height, x, and y integer values.
        """
        with self.assertRaises(TypeError):
            Rectangle(2.3, 4.5)

        with self.assertRaises(TypeError):
            Rectangle('10', 23)

        with self.assertRaises(TypeError):
            Rectangle(10, [8])

        with self.assertRaises(TypeError):
            Rectangle(3, 3, '0.2', '0.5')

        with self.assertRaises(TypeError):
            Rectangle(3, 3, 0.2, 0.5)

    def test_wrong_values(self):
        """Rectangle object initialization with non-integer width
        height, x, and y arguments.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0)

        with self.assertRaises(ValueError):
            Rectangle(-1, -2, 8, 9)

        with self.assertRaises(ValueError):
            Rectangle(10, 11, 0, -2)

        with self.assertRaises(ValueError):
            Rectangle(2, 4, -1, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, -21)

        with self.assertRaises(ValueError):
            Rectangle(10, 0)


class TestRectangleMethods(unittest.TestCase):
    """Unit tests for method functionality of Rectangle instance."""

    def test_area(self):
        """Test the area of Rectangle instance."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 2).area(), 56)

    def test_display(self):
        """Test the display of Rectangle object in stdout."""
        tmpout = StringIO()
        sys.stdout = tmpout

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(tmpout.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        sys.stdout = sys.__stdout__

    def test_update(self):
        """Test the update method of Rectangle instance."""
        tmpout = StringIO()
        sys.stdout = tmpout

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        print(r1)
        self.assertEqual(tmpout.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle instance."""
        rectangle1 = Rectangle(12, 9, 1, 3, 78)
        self.assertEqual(rectangle1.to_dictionary(),
                         {"id": 78, "width": 12, "height": 9, "x": 1, "y": 3})

    def test_save_to_file(self):
        """Test save_to_file method."""
        filename = "Rectangle.json"
        r1 = Rectangle(10, 7, 2, 8, 85)
        r2 = Rectangle(2, 4, 0, 0, 15)
        Rectangle.save_to_file([r1, r2])

        with open(filename, "r") as file:
            self.assertListEqual(json.loads(file.read()), [
                {"y": 8, "x": 2, "id": 85, "width": 10, "height": 7},
                {"y": 0, "x": 0, "id": 15, "width": 2, "height": 4}
            ])
        os.remove(filename)

    def test_create(self):
        """Test create method."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()

        self.assertDictEqual(r1_dictionary, r2_dictionary)

    def test_load_from_file(self):
        """Test load_from_file method."""
        filename = "Rectangle.json"
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

        self.assertListEqual([], Rectangle.load_from_file())

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(2, len(list_rectangles_output))

        for obj in list_rectangles_output:
            self.assertIsInstance(obj, Rectangle)

        for entry in enumerate(list_rectangles_output):
            self.assertDictEqual(
                list_rectangles_input[entry[0]].to_dictionary(),
                entry[1].to_dictionary())


if __name__ == "__main__":
    unittest.main()
