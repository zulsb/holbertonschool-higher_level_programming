#!/usr/bin/python3
"""
    Tests class Square.
"""
import unittest
import sys
import pep8
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import models.base
import models.rectangle
import models.square


class T_Square(unittest.TestCase):
    """ Tests class square. """

    def t_sty_square(self):
        """ Tests. """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
        p = style.check_files(['models/square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def t_id(self):
        """ Test id. """
        self.assertTrue(self.s1.id, 1)
        self.assertTrue(self.s2.id, 2)

    def t_attr_square(self):
        """ Test attr square. """
        with self.assertRaises(TypeError):
            Square('A')
        with self.assertRaises(ValueError):
            Square(-4)
        with self.assertRaises(ValueError):
            Square(size=1, x=-1)
        with self.assertRaises(TypeError):
            Square(size=1, y='A')

    def t_update(self):
        """ Test update. """
        tmp = Square(5)
        tmp.update(10)
        self.assertEqual(str(tmp), '[Square] (10) 0/0 - 5')
        tmp.update(1, 2)
        self.assertEqual(str(tmp), '[Square] (1) 0/0 - 2')
        tmp.update(1, 2, 3)
        self.assertEqual(str(tmp), '[Square] (1) 3/0 - 2')

    def t_dict(self):
        """ Test dictionary. """
        Base._Base__nb_objects = 0
        r1 = Square(2, 2, 2, 2)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 2, 'y': 2, 'size': 2, 'id': 2})
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 1})

    def checking(self):
        """ Test check. """
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(size.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

    @classmethod
    def set_up(cls):
        """ Test set up. """
        Base._Base__nb_objects == 0
        cls.s1 = Square(2, 2)
        cls.s2 = Square(size=4, x=2, y=3)

    def t_area(self):
        """ Test area. """
        self.assertTrue(self.s1.area(), 4)
        self.assertTrue(self.s2.area(), 16)

    def t_str(self):
        """ Test str. """
        self.assertEqual(str(self.s1), '[Square] (3) 2/0 - 2')
        self.assertEqual(str(self.s2), '[Square] (4) 2/3 - 4')

    def t_display(self):
        """ Test display. """
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r1 = Square(4)
        r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n####\n####\n")
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(2, 2, 2, 2)
        r1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main()
