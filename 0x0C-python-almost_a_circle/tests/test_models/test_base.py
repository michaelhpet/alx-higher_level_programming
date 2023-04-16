#!/usr/bin/python3
"""Test Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

    def test_without_id(self):
        """Test for instantiation of base class without id."""
        new_object = Base()
        self.assertEqual(new_object.id, 1)

        another_object = Base()
        self.assertEqual(another_object.id, 2)

    def test_iteration_without_id(self):
        """Test for iterative instantiation without id."""
        for i in range(5):
            new_object = Base()
            self.assertEqual(new_object.id, i + 1)

    def test_with_id(self):
        """Test for instantiation of Base class with an id argument."""
        new_object = Base(12)
        self.assertEqual(new_object.id, 12)

    def test_iteration_with_id(self):
        """Test for iterative instantiation with an id argument."""
        for number in [12, 43, 32, 56, 17]:
            new_object = Base(number)
            self.assertEqual(new_object.id, number)

    def test_with_non_number(self):
        """Test for instantiation with a non-number argument"""
        self.assertEqual(Base([]), 1)
        self.assertEqual(Base('3'), 2)
        self.assertEqual(Base(True), 3)


if __name__ == "__main__":
    unittest.main()
