#!/usr/bin/python3
"""
    Module to creates the function that adds 2 integers
    
"""
def add_integer(a, b=98):
    """ Function adds 2 integers
        Args:
        a: num int
        b: num int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        in_ab = int(a) + int(b)
        return in_ab
