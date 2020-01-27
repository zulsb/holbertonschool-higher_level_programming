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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Is one of the standard formats for sharing data representation.
            Args:
                list_dictionaries: Is a list of dictionaries.
        """
        if not list_dictionaries or len(list_dictionaries) is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ That writes the JSON string representation of list_objs to a file.
            Args:
                cls: Reference class.
                list_objs: List objects.
        """
        new_lts = []

        if list_objs is not None:
            for i in list_objs:
                new_lts.append(cls.to_dictionary(i))

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as fl:
            fl.write(cls.to_json_string(new_lts))

    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.
            Args:
                json_string: Is a string representing a list of dictionaries.
        """
        if not json_string or len(json_string) is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set.
            Args:
                cls: Class.
                dictionary: Dictionary.
        """
        if cls.__name__ == "Rectangle":
            o = cls(1, 1)
        else:
            o = cls(1)
        o.update(**dictionary)
        return o

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances.
            Args:
                cls: Current class.
        """
        try:
            with open(cls.__name__ + ".json", "r") as fl:
                new_dic = cls.from_json_string(fl.read())

                r_es = []
                for i in new_dic:
                    r_es.append(cls.create(**i))
                return r_es
        except FileNotFoundError:
            return []
