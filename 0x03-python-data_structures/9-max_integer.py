#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for m in my_list:
            if m > max_int:
                max_int = m
        return (max_int)
    else:
        return (my_list, None)	    
