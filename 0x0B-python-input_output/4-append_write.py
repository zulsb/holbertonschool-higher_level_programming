#!/usr/bin/pyhton3
"""
    Module contains the append_write function.
"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file (UTF8).
        Args:
            filename: Text file.
            text: Text to write.
    """
    with open(filename, mode="a", encoding="utf-8") as fl:
        return(fl.write(text))
