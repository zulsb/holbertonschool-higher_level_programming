#!/usr/bin/python3
"""
    Module contain the class BaseGeometry.
"""


class BaseGeometry():
    """ Geometry class. """

    def area(self):
        """ Function area exception. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function integer validation.
            Args:
            name: Name value.
            value: Value.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
