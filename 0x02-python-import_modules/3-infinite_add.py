#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_num = 0
    for a in argv[1:]:
        arg_num += int(a)
    print(arg_num)
