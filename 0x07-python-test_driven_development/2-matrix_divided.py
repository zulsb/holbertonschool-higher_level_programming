#!/usr/bin/python3
"""
    Module contains the matrix_divided function.

"""


def matrix_divided(matrix, div):
    """ Function that divides contents of matrix by div.
        Args:
        matrix: matrix of elements
        div: divisor
    """

    size = len(matrix[0])
    for rw in matrix:
        if len(rw) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    r_d = []
    count = 0
    for mbr in matrix:
        if not isinstance(mbr, list):
            raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")

        r_d.append([])

        for i in mbr:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
            r_d[count].append(round(i / div, 2))
        count += 1

    return r_d
