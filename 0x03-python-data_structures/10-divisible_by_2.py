#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_lis = my_list.copy()
    for m in range(len(n_lis)):
        if (my_list[m] % 2) == 0:
            n_lis[m] = True
        else:
            n_lis[m] = False
    return n_lis
