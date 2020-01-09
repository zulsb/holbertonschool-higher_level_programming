#!/usr/bin/python3
class Square():
    """ This is a class Square that defines a square
    with a private instance attribute: size """
    def __init__(self, size=0):
        """Special method, initialize object attributes
        Args:
            size: Private instance attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
