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
    if isinstance(obj, a_class):
        if type(obj) is a_class:
            return False
        else:
            return True
    return False
