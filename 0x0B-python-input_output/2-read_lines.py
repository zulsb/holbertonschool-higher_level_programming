#!/usr/bin/python3
"""
    Module contains the read_lines function.
"""


def read_lines(filename="", nb_lines=0):
    """ Function that reads n lines of a text file (UTF8).
        Args:
            filename: Text file.
            nb_lines: Number lines.
    """
    with open(filename, mode="r", encoding="utf-8") as fl:
        if nb_lines <= 0:
            print(fl.read(), end="")
        else:
            lines_fl = fl.readlines()
            c = 0
            for i in lines_fl:
                if nb_lines is c:
                    break
                c += 1
                print(i, end="")
