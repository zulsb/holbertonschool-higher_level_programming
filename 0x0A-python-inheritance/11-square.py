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


class Rectangle(BaseGeometry):
    """ Rectangle class. """
    def __init__(self, width, height):
        """ Module inicializer.
            Args:
            width: Rectangle width.
            height: Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Function to get area of rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Function to return string rectangle. """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Square class. """
    def __init__(self, size):
        """ Module to initializer.
            Args:
            size: Size of square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        """ Return the area os a square. """
        return self.size * self.size

    def __str__(self):
        """ Return the string square. """
        return("[Square] {0:d}/{0:d}".format(self.size, self.size))
