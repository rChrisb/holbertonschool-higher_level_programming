#!/usr/bin/python3
"""Area of a square"""


class Square:
    """class Square that defines a square
    by Private instance attribute: size
    with Instantiation with optional size
    and a Public instance method: def area(self)
    that returns the current square area """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
