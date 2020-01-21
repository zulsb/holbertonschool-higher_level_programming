#!/usr/bin/python3
"""
    Module contains the save_to_json_file function.
"""


import json


def save_to_json_file(my_obj, filename):
    """ Function that returns the JSONrepresentation of an object (string).
        Args:
            my_obj: Object.
            filename: Text name.
    """
    with open(filename, mode="w", encoding="utf-8") as fl:
        return fl.write(json.dumps(my_obj))
