#!/usr/bin/python3
"""
    Module contains the class_to_json function.
"""


def class_to_json(obj):
    """ Function returns the dictionary description with simple data structure.
        Args:
            obj: Object.
    """
    return(obj.__dict__)
