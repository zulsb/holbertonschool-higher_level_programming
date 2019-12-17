#!/usr/bin/python3
def print_list_integer(my_list=[]):
    longi = len(my_list)	
    for i in range(longi + 1):
        print("{:d}".format(i))
