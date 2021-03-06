#!/usr/bin/python3
"""
   Modulo contains a class
   Rectangle that defines a rectangle.
"""


class Rectangle():
    """ Class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Method to initialize object attributes
            Args:
                width: Width of rectangle.
                height: Height of rectangle. """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Return the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method to get a value width
            Args:
                value: Private instance attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Return the height of value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method to get a value height.
            Args:
                value: Private instance attribute """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
