#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lines in range(len(matrix)):
        for integers in range(len(matrix[lines])):
            if integers == len(matrix[lines]) - 1:
                print("{:d}".format(matrix[lines][integers]), end="")
            else:
                print("{:d}".format(matrix[lines][integers]), end=" ")
        print()
