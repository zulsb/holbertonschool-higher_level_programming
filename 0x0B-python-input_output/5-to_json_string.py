#!/usr/bin/python3
"""
    Module contains the to_json_string function.
"""


import json


def to_json_string(my_obj):
    """ Function that returns the JSONrepresentation of an object (string).
        Args:
            my_obj: Object.
    """
    return(json.dumps(my_obj))
