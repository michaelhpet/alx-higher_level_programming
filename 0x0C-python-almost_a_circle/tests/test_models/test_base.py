#!/usr/bin/python3
"""Test module for Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """Unit tests for base objects."""

    def test_without_id(self):
        """Test for instantiation of base class without id."""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base()
        self.assertEqual(base1.id, base2.id - 1)
        self.assertGreater(base4.id, base3.id)
        self.assertEqual(base4.id, base1.id + 3)

    def test_with_id(self):
        """Test for instantiation of Base class with an id argument."""
        base1 = Base(12)
        base2 = Base(54)
        self.assertEqual(base1.id, 12)
        self.assertEqual(base2.id, 54)
        self.assertNotEqual(base1.id, base2.id)

    def test_to_json_string(self):
        """Test to_json_string static method."""
        rectangle_dict = Rectangle(42, 21, 3, 3, 77).to_dictionary()
        square_dict = Square(13, 1, 4, 78).to_dictionary()
        rectangle_json = Base.to_json_string([rectangle_dict])
        square_json = Base.to_json_string([square_dict])

        self.assertDictEqual(json.loads(rectangle_json)[0], rectangle_dict)
        self.assertDictEqual(json.loads(square_json)[0], square_dict)


if __name__ == "__main__":
    unittest.main()
