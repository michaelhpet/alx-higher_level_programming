#!/usr/bin/python3
"""Test module for Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle objects."""

    def test_rectangle_instance(self):
        """Rectangle object is an instance of Rectangle class."""
        rectangle1 = Rectangle(20, 10)
        self.assertIsInstance(rectangle1, Rectangle)

    def test_base_instance(self):
        """Rectangle object is an instance of Base class."""
        rectangle1 = Rectangle(15, 12)
        self.assertIsInstance(rectangle1, Base)

    def test_coordinates(self):
        """Test for coordinates attributes."""
        rectangle1 = Rectangle(15, 10)
        rectangle2 = Rectangle(18, 11, 15, 71)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.x, rectangle1.y)

        self.assertEqual(rectangle2.x, 15)
        self.assertEqual(rectangle2.y, 71)
        self.assertNotEqual(rectangle2.x, rectangle2.y)

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


if __name__ == "__main__":
    unittest.main()
