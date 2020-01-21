#!/usr/bin/python3
"""
    Module contains the number_of_lines function.
"""


def number_of_lines(filename=""):
    """ Function returns the number of lines of a text file.
        Args:
            filename: Text file.
    """
    with open(filename, mode="r", encoding="utf-8") as fl:
        return(len(fl.readlines()))
