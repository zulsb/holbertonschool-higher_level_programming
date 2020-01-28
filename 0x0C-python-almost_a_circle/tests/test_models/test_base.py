#!/usr/bin/python3
"""
    Tests class Base.
"""
import io
import unittest
import importlib
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.base
import models.rectangle
import models.square


class Test_Base(unittest.TestCase):
    """Class test class base."""

    def set_Up(self):
        """Setup for reseting. """
        Base._Base__nb_objects = 0
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_au_id(self):
        """test. """
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_spec_id(self):
        """assigned id. """
        a = Base(8)
        self.assertEqual(a.id, 8)
