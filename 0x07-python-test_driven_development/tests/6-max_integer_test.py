#!/usr/bin/python3
"""This module contains unit tests for the function \
max integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains unit tests for max_integer"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([34, 65, 78, 78, 2]), 78)
        self.assertEqual(max_integer([4.0, 5.3, 3.9, 6.4, 2.9]), 6.4)
        self.assertEqual(max_integer([-3, -4, -6, -4, -9]), -3)
        self.assertRaises(TypeError, max_integer, [1, 3, 'school', 79])
        self.assertRaises(TypeError, max_integer, [1, 2, 4, [6, 8, 4]])


if __name__ == "__main__":
    unittest.main()
