#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        max_val = max_integer([0, 500, 200, -650])
        self.assertEqual(max_val, 500, "The max is wrong")

    def test_type(self):
        self.assertIsInstance(a, b)	



if __name__ == '__main__':
    unittest.main()