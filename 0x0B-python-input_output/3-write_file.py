#!/usr/bin/python3
"""
    Module contains the write_file function.
"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file (UTF8).
        Args:
            filename: Text file.
            text: Text to write.
    """
    with open(filename, mode="w", encoding="utf-8") as fl:
        return(fl.write(text))
