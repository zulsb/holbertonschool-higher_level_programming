#!/usr/bin/python3
"""
    Module contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """ Function same class or inherit from.
        Args:
        obj: Object.
        a_class: Class.
    """
    if not type(obj) is a_class:
        if issubclass(type(obj), a_class):
            return True
        else:
            return False
