#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for t in range(len(matrix)):
        for x in range(len(matrix[0])):
            n[t][x] = pow(matrix[t][x], 2)
    return n
