#!/usr/bin/python3
"""
   Modulo contains print_square function.

"""


def print_square(size):
    """ Function that prints a square with the character #.
        Args:
        size: Is the size length of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
