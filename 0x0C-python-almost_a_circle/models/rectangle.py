#!/usr/bin/python3
"""
    Module contains Rectangle class that inherits from Base.
"""
from .base import Base


class Rectangle(Base):
    """ This class will be the “base” of all other classes in this project.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor.
            Args:
                width: Rectangle width.
                height: Rectangle height.
                x: Position x.
                y: Position y.
                id: Identifier.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get the width of rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of rectangle.
            Args:
                value: Value rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of rectangle.
            Args:
                value: Value rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the position x of rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the position x of rectangle.
            Args:
                value: Value rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the position y of rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the position y of rectangle.
            Args:
                value: Value rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of rectangle. """
        return self.width * self.height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character #. """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Returns string of rectangle. """
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ That assigns an argument to each attribute.
            Args:
                args: Attribute tuple of rectangle.
        """
        if args:
            ar = ["id", "width", "height", "x", "y"]
            for k, v in zip(ar, args):
                setattr(self, k, v)
        else:
            ar = ["id", "width", "height", "x", "y"]
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k in ar:
                        setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle. """
        dinary = {}
        ar = ["id", "width", "height", "x", "y"]

        for i in ar:
            dinary[i] = getattr(self, i)
        return(dinary)
