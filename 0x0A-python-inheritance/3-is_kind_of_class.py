#!/usr/bin/python3
"""
    Module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """ Function same class or inherit from.
        Args:
        obj: Object.
        a_class: Class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
