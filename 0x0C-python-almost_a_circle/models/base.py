#!/usr/bin/python3
"""
    Module contains Base class.
"""


class Base():
    """ This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor:
            Args:
                id: Identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
