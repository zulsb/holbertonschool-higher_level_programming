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

    def to_json(self):
        return self.__dict__
