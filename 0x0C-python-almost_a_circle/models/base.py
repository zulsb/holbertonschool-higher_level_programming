#!/usr/bin/python3
"""
    Module contains Base class.
"""
import json


class Base():
    """ This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Function constructor:
            Args:
                id: Identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Is one of the standard formats for sharing data representation.
            Args:
                list_dictionaries: Is a list of dictionaries.
        """
        if not list_dictionaries or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)
