#!/usr/bin/python3
"""
    Module contains the function read_file.
"""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout.
        Args:
            filename: File name to read.
    """
    with open(filename, mode="r", encoding="utf-8") as fl:
        print(fl.read(), end="")
