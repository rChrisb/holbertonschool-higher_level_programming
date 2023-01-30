#!/usr/bin/python3

""" Access and update private attribute"""


class Square:
    """class Square that defines a square
    by Private instance attribute: size
    with Instantiation with optional size
    and a Public instance method: def area(self)
    that returns the current square area """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
