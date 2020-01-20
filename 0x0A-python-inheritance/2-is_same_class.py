#!/usr/bin/python3
"""
    Module contain the function is_same_class.
"""


def is_same_class(obj, a_class):
    """ Function to compare if exact same object
        Args:
        obj:
        a_class:
    """
    if type(obj) is a_class:
        return True
    else:
        return False
