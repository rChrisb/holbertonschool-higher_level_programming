#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda line: list(map(lambda element: element ** 2, line)), matrix)))
