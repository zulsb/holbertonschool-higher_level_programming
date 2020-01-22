#!/usr/bin/python3
"""
    Module contains the Student class.
"""


class Student:
    """ Defines a first_name, last_name and age of student. """

    def __init__(self, first_name, last_name, age):
        """ Module constructor inicialize.
            Args:
            first_name: First name.
            last_name: Last name.
            age: Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ That retrieves a dictionary representation of a Student instance.
            Args:
                attrs: Is a list of strings.
        """
        if attrs is None:
            return self.__dict__
        else:
            lt_st = {}

            for i_key in attrs:
                if i_key in self.__dict__:
                    lt_st[i_key] = self.__dict__[i_key]

            return lt_st
