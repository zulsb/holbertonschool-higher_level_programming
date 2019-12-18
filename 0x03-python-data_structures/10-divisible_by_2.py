#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_lis = my_list.copy()
    for m in n_lis:
        if (n_lis[m] % 2) == 0:
            n_lis[m] = True
        else:
            n_lis[m] = False
    return n_lis
