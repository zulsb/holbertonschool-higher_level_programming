#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
        exit()
    arg_num = len(argv) - 1
    if len(argv) == 2:
        print("{} argument:".format(arg_num))
    else:
        print("{} arguments:".format(arg_num))

    for num in range(1, len(argv)):
        print("{}: {}".format(num, argv[num]))
