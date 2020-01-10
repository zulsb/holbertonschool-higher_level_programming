#!/usr/bin/python3
class Square():
    """ This is a class Square that defines a square
    with a private instance attribute: size """

    def __init__(self, size=0):
        """ Method to initialize object attributes"""
        self.size = size

    @property
    def size(self):
        """ Return the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to get a value size
        Args:
            value: Private instance attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method to get a area square """
        return self.size * self.size

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.size == 0:
            print()
        else:
            for r in range(self.__size):
                print("#" * self.size)
