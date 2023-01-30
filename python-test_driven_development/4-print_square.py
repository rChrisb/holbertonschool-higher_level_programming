#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """function that prints a square with the character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        for x in range(size):
            if x == size - 1:
                print("#")
            else:
                print("#", end="")
