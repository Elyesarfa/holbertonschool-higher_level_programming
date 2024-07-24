#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this is the class for unittest"""

    def test_max(self):
        """function to verify max of the list"""
        self.assertEqual(max_integer([1, 2, 3, 200, 1000, -2, -2000]), 1000)

    def test_none(self):
        """check if the function returns None if the list is empty"""
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
