#!/usr/bin/python3
"""
    Module contains the from_json_string function.
"""


import json


def from_json_string(my_str):
    """ Function that returns the JSONrepresentation of an object (string).
        Args:
            my_str: Strings.
    """
    return(json.loads(my_str))
