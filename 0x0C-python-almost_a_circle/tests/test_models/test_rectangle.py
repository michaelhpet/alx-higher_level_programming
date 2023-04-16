#!/usr/bin/python3
"""Test module for Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


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


if __name__ == "__main__":
    unittest.main()
