#!/usr/bin/python3
"""
   Module contains text_indentation function.

"""


def text_indentation(text):
    """ Function that prints a text with new lines to
        characters: ., ? and :
        Args:
        text: Text.
    """

    ini = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for idx, ite in list(enumerate(text)):
        if ite in ".?:":
            t = text[ini: idx + 1].strip()
            print("{}". format(t), end="\n\n")
            ini = idx + 1

    if ini < len(text):
        s = text[ini:].strip()
        print("{}". format(s), end="")
