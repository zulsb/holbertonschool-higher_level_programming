#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for e in range(x):
            print(my_list[e], end="")
            i += 1
        print()
    except:
        print()
    return i
