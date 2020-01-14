#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_Empty_lts(self):
        l = []
        self.assertEqual(max_integer(l), None)

    def test_docstr(self):
        self.assertIsNotNone(max_integer.__doc__)

    def test_Normal(self):
        l = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(l), 5)

    def test_elem(self):
        l = [5]
        self.assertEqual(max_integer(l), 5)

    def test_str_int(self):
        self.assertRaises(TypeError, max_integer, ["a", "b", 1])

    def test_neg(self):
        self.assertEqual(max_integer([-2, -1]), -1)

    def test_negative_zero(self):
        l = [0, -1]
        self.assertEqual(max_integer(l), 0)

    def test_wds(self):
        l = ["hello", "hi", "bye"]
        self.assertEqual(max_integer(l), "hi")

    def test_dictor(self):
        l = {0: "a", 1: "b", 2: "c"}
        self.assertEqual(max_integer(l), "c")


if __name__ == '__main__':
    unittest.main()
