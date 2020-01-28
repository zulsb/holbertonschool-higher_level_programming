#!/usr/bin/python3
"""
    Tests class Rectangle.
"""
import unittest
import sys
import pep8
import io
from models.base import Base
from models.rectangle import Rectangle
import importlib
from contextlib import redirect_stdout
import models.base
import models.rectangle


class test_Rectangle(unittest.TestCase):
    """ Tests class Rectangle. """

    def t_sty_rect(self):
        """ Tests for pep8. """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def t_ids(self):
        """ Test id. """
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.r3.id = "a"
        self.assertEqual(self.r3.id, "a")

    def t_area(self):
        """ Test area. """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 8)

    def t_str(self):
        """ Test str. """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (2) 0/0 - 10/2")
        self.assertEqual(self.r3.__str__(), "[Rectangle] (a) 2/2 - 2/4")

    def t_dictionary(self):
        """ Test dictionary. """
        r1_dictionary = self.r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 0, 'y': 0, 'width': 10, 'height': 2, 'id': 2})
        r3_dictionary = self.r3.to_dictionary()
        self.assertDictEqual(r3_dictionary, {
            'x': 2, 'y': 2, 'width': 2, 'height': 4, 'id': 12})

    def chck_docstr(self):
        """ Test check docstr. """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(width.__doc__)
        self.assertIsNotNone(height.__doc__)
        self.assertIsNotNone(x.__doc__)
        self.assertIsNotNone(y.__doc__)
        self.assertIsNotNone(area.__doc__)
        self.assertIsNotNone(display.__doc__)
        self.assertIsNotNone(__str__.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

    @classmethod
    def set_up(cls):
        """ Test """
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(10, 2)
        cls.r3 = Rectangle(2, 4, 2, 2, 12)

    def t_attr_err(self):
        """ Tests. """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r11 = Rectangle(10, "2")
        with self.assertRaises(ValueError, msg="height must be  > 0"):
            r11 = Rectangle(-2, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r11 = Rectangle({1: 2}, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r21 = Rectangle(10, 2)
            r21.width = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r31 = Rectangle(10, 2)
            r31.x = {}
        with self.assertRaises(ValueError, msg="y must be >=0"):
            r41 = Rectangle(10, 2, 3, -1)

    def t_display(self):
        """ Tests display. """
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "##########\n##########\n")
        sys.stdout = mystdout = StringIO()
        self.r3.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def t_update(self):
        """" Test update. """
        self.r1.update(89)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 10/2")
        self.r1.update(89, 2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/2")
        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/3")
        self.r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            self.r1.update(y=1, width=2, x=-3, id=89)

    def t_json(self):
        """ Test json. """
        dict = self.r1.to_dictionary()
        self.assertIsInstance(Base.to_json_string(dict), str)


if __name__ == '__main__':
    unittest.main()
