#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = my_list.copy()
    for t in range(len(my_list)):
        if n[t] == search:
            n[t] = replace
    return n
