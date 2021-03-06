#!/usr/bin/python3
"""
   Modulo contains a class
   Rectangle that defines a rectangle.
"""


class Rectangle():
    """ Class that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method to initialize object attributes
            Args:
                width: Width of rectangle.
                height: Height of rectangle. """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Method to get rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Method to get a ractangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Method to print a rectangle."""
        str_ing = ""
        if self.width == 0 or self.height == 0:
            return str_ing

        for i in range(self.height):
            str_ing += self.width * str(self.print_symbol)
            if i + 1 != self.height:
                str_ing += "\n"

        return str_ing

    def __repr__(self):
        """ Method to representation rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Method detect instance deletion of Rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method returns the biggest rectangle based on the area. """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ Method that returns a new Rectangle instance. """
        return cls(size, size)
