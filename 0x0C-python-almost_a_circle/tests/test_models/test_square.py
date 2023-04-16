#!/usr/bin/python3
"""Test module for Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys
import json
import os


class TestSquareInstance(unittest.TestCase):
    """Unit tests for instantiation of Square objects."""

    def test_square_instance(self):
        """Square object is an instance of Square class."""
        square1 = Square(20)
        self.assertIsInstance(square1, Square)

    def test_rectangle_instance(self):
        """Square object is an instance of Rectangle class."""
        square1 = Square(15)
        self.assertIsInstance(square1, Rectangle)

    def test_base_instance(self):
        """Square object is an instance of Base class."""
        square1 = Square(11)
        self.assertIsInstance(square1, Base)

    def test_str(self):
        """Test the informal representation of Square object."""
        square1 = Square(6, 2, 1, 12)
        self.assertEqual(square1.__str__(), "[Square] (12) 2/1 - 6")

    def test_id(self):
        """Test for id attribute."""
        for id in [12, 56, 8, 19]:
            square = Square(15, 8, 13, id)
            self.assertEqual(square.id, id)

        square1 = Square(18, 0, 2)
        square2 = Square(21, 1, 1)
        square3 = Square(34, 9, 7)
        square4 = Square(5)
        square5 = Square(13)

        self.assertEqual(square1.id, square2.id - 1)
        self.assertEqual(square3.id, square2.id + 1)
        self.assertEqual(square1.id, square5.id - 4)
        self.assertGreater(square4.id, square3.id)

    def test_without_dimensions(self):
        """Square object initialization without size argument."""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(None, 1, 3)

    def test_coordinates(self):
        """Test for coordinates attributes."""
        square1 = Square(15)
        square2 = Square(18, 15, 71)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.x, square1.y)

        self.assertEqual(square2.x, 15)
        self.assertEqual(square2.y, 71)
        self.assertNotEqual(square2.x, square2.y)

        with self.assertRaises((ValueError, TypeError)):
            Square(10, -2.5, 10)

        with self.assertRaises((ValueError, TypeError)):
            Square(12, -0.5, -11)

    def test_wrong_types(self):
        """Square object initialization with non-integer size, x,
        and y arguments.
        """
        with self.assertRaises(TypeError):
            Square(2.3)

        with self.assertRaises(TypeError):
            Square('10')

        with self.assertRaises(TypeError):
            Square([8])

        with self.assertRaises(TypeError):
            Square(3, '0.2', '0.5')

        with self.assertRaises(TypeError):
            Square(3, 0.2, 0.5)

    def test_wrong_values(self):
        """Square object initialization with invalid size,
        x, and y integer values.
        """
        with self.assertRaises(ValueError):
            Square(0, 0, 0)

        with self.assertRaises(ValueError):
            Square(-1, 8, 9)

        with self.assertRaises(ValueError):
            Square(11, 0, -2)

        with self.assertRaises(ValueError):
            Square(4, -1, 5)

        with self.assertRaises(ValueError):
            Square(10, -21)

        with self.assertRaises(ValueError):
            Square(0)


class TestSquareMethods(unittest.TestCase):
    """Unit tests for method functionality of Square instance."""

    def test_area(self):
        """Test the area of Square instance."""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(10).area(), 100)
        self.assertEqual(Square(8, 0, 0, 2).area(), 64)

    def test_display(self):
        """Test the display of Square object in stdout."""
        tmpout = StringIO()
        sys.stdout = tmpout

        r1 = Square(3, 2, 2)
        r1.display()
        self.assertEqual(tmpout.getvalue(), "\n\n  ###\n  ###\n  ###\n")

        sys.stdout = sys.__stdout__

    def test_update(self):
        """Test the update method of Square instance."""
        tmpout = StringIO()
        sys.stdout = tmpout

        r1 = Square(10, 10, 10)
        r1.update(89)
        print(r1)
        self.assertEqual(tmpout.getvalue(), "[Square] (89) 10/10 - 10\n")

        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle instance."""
        square1 = Square(12, 1, 4, 101)
        self.assertEqual(square1.to_dictionary(),
                         {"id": 101, "size": 12, "x": 1, "y": 4})

    def test_save_to_file(self):
        """Test save_to_file method."""
        filename = "Square.json"
        s1 = Square(10, 2, 8, 14)
        s2 = Square(4, 0, 0, 8)
        Square.save_to_file([s1, s2])

        with open(filename, "r") as file:
            self.assertListEqual(json.loads(file.read()), [
                {"y": 8, "x": 2, "id": 14, "size": 10},
                {"y": 0, "x": 0, "id": 8, "size": 4}
            ])
        os.remove(filename)

    def test_create(self):
        """Test create method."""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()

        self.assertDictEqual(s1_dictionary, s2_dictionary)

    def test_load_from_file(self):
        """Test load_from_file method."""
        filename = "Square.json"
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

        self.assertListEqual([], Square.load_from_file())

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(2, len(list_squares_output))

        for obj in list_squares_output:
            self.assertIsInstance(obj, Square)

        for entry in enumerate(list_squares_output):
            self.assertDictEqual(list_squares_input[entry[0]].to_dictionary(),
                                 entry[1].to_dictionary())


if __name__ == "__main__":
    unittest.main()
