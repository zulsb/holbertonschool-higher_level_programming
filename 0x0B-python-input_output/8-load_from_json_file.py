#!/usr/bin/python3
"""
    Module contains the load_from_json_file function.
"""


import json


def load_from_json_file(filename):
    """ Function that that creates an Object from a “JSON file”.
        Args:
            filename: Text name.
    """
    with open(filename, mode="r", encoding="utf-8") as fl:
        return json.loads(fl.read())
