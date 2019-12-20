#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    new = my_list.copy()
    n = list(map(lambda mul: mul * number, new))
    return n
