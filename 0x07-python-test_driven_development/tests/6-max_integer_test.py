#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test for max_integer function
    """
    def test_empty_list(self):
        """test for empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """test for negative numbers"""
        self.assertEqual(max_integer([-1, -8, -2981]), -1)

    def test_positive_numbers(self):
        """test for positive numbers"""
        self.assertEqual(max_integer([18289, 276, 0, 2]), 18289)

    def test_equal_numbers(self):
        """test for list of equal numbers"""
        self.assertEqual(max_integer([2, 2, 2.0]), 2)
