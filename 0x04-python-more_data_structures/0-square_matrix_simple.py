#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = [copy[:] for copy in matrix]
    for t in range(len(matrix)):
        for x in range(len(matrix[0])):
            n[t][x] = pow(matrix[t][x], 2)
    return n
