#!/usr/bin/python3
"""
    Module contains say_my_name function to print
    first and last name.
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>.
        Args:
        first_name: First name.
        last_name: Last name.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    else:
        print("My name is {} {}".format(first_name, last_name))
