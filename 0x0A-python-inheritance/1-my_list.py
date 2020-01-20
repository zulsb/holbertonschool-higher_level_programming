#!/usr/bin/python3
"""
    Module contains the MyList class.
"""


class MyList(list):
    """ Subclass inherits from list. """
    def print_sorted(self):
        """ Function to print list in sorted order. """
        print(sorted(self))
