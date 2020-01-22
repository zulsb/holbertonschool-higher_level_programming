#!/usr/bin/python3
"""
    Module contain the class BaseGeometry.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class. """
    def __init__(self, size):
        """ Module to initializer.
            Args:
            size: Size of square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Return the area os a square. """
        return self.__size * self.__size
