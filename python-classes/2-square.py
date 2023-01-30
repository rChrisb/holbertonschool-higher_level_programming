#!/usr/bin/python3
"""Square validation"""


class Square:
    """class Square that defines a square
    by Private instance attribute: size
    with Instantiation with optional size"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
