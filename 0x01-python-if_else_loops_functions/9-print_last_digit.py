#!/usr/bin/python3
def print_last_digit(number):
    final = abs(number) % 10
    print("{:d}".format(final), end="")
    return final
