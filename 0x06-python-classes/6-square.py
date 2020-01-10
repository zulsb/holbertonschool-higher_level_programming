#!/usr/bin/python3
class Square():
    """ This is a class Square that defines a square
    with a private instance attribute: size """

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize object attributes
            Args:
            size: Size of square
            position: square position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Return the position """
        return self.__position

    @position.setter
    def position(self, value):
        """Method to get a value size
        Args:
            value: Private instance attribute """
        if isinstance(value, tuple) and len(value) == 2 and \
            isinstance(value[0], int) and isinstance(value[1], int)\
                and value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Method to get a area square """
        return self.size * self.size

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for r in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
