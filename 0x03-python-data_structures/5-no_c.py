#!/usr/bin/python3
def no_c(my_string):
    return my_string.translate({ord(m): None for m in "cC"})
