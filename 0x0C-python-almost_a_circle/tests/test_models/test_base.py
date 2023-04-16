#!/usr/bin/python3
"""Test Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

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


if __name__ == "__main__":
    unittest.main()
