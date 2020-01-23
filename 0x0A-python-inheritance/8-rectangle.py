#!/usr/bin/python3
"""
    Module contain the class BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class. """
    def __init__(self, width, height):
        """ Module inicializer.
            Args:
            width: Rectangle width.
            height: Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
