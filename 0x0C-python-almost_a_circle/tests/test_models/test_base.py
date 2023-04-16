#!/usr/bin/python3
"""
test_base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Tests for Base classss
    """

    def test_without_id(self):
        """
        Tests for instantiation of base class without id
        """
        object = Base()
        self.assertEquals(object.id, 1)


if __name__ == "__main__":
    unittest.main()
