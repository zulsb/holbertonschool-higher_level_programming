#!/usr/bin/python3
"""
    Module contain the functin lookup.
"""


def lookup(obj):
    """ Function returns the list of available
        attributes and methods of an object.
        Args:
        obj: Object.
    """
    return dir(obj)
