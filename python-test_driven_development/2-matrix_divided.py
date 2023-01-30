#!/usr/bin/python3
"""Divide a matrix
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for line in matrix:
        for element in line:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
    return (list(map(lambda line: list(map(lambda e: round(e / div, 2), line)), matrix)))
