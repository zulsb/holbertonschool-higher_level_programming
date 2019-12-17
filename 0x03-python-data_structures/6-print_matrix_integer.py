#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for t in range(len(matrix[0])):
            print("{:d}".format(matrix[m][t]), end="")
            if t + 1 < len(matrix[0]):
                print(" ", end="")
        print()
