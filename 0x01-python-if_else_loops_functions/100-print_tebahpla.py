#!/usr/bin/python3

for alpah in range(122, 96, -1):
    if alpah % 2 != 0:
        alpah = alpah - 32
    print("{:c}".format(alpah), end="")
