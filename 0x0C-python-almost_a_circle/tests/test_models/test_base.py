#!/usr/bin/python3
"""
    Tests class Base.
"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle


class Test_Base_(unittest.TestCase):
    """ Tests class Base. """
    def st_u(self):
        """ Runs before each unittest. """
        Base._Base__nb_objects = 0

    def t_init_empty_id(self):
        """ Test init empty id. """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def t_cls_docstr(self):
        """ Test class docstr. """
        self.assertIsNotNone(Base.__doc__)

    def t_pep8(self):
        """ Test pep8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/base.py"])
        self.assertEqual(pep.total_errors, 0)

    def t_init_non_empty_id(self):
        """ Test init non empty id. """
        self.assertTrue(Base(42), 42)

    def t_init_tr_inst(self):
        """ Test init 3 instances. """
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 42)
        self.assertTrue(b3.id == 2)

    def t_init_tw_inst(self):
        """ Test init 2 instances. """
        b1 = Base(42)
        b2 = Base()
        self.assertTrue(b1.id == 42)
        self.assertTrue(b2.id == 1)

if __name__ == '__main__':
    unittest.main()
