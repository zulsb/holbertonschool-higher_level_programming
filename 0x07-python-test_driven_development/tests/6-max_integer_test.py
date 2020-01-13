#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_Empty_lts(self):
        l = []
        self.assertEqual(max_integer(l), None)


if __name__ == '__main__':
    unittest.main()
