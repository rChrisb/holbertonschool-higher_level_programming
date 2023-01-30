#!/usr/bin/python3
"""  Integers addition """


def add_integer(a, b=98):
    """Write a function that adds 2 integers
    """

    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a + b)
    # if a is None or b is None:
    #     return
    # try:
    #     sum = a + b
    #     return int(sum)
    # except TypeError:
    #     if type(a) is not int:
    #         print("a must be an integer")
    #     elif type(b) is not int:
    #         print("b must be an integer")
