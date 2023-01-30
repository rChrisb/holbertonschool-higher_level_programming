#!/usr/bin/python3

""" Printing a square"""


class Square:
    """class Square that defines a square
    by Private instance attribute: size
    with Instantiation with optional size
    and a Public instance method: def area(self)
    that returns the current square area and
    with Public instance method: def my_print(self)"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1] == 1:
            print()
        elif self.__position[1] > 1 and self.size > 0:
            print("\n"*self.__position[1], end="")
        for n in range(self.__size):
            print(" "*self.__position[0], end="")
            for x in range(self.size):
                if x == self.size - 1:
                    print("#")
                else:
                    print("#", end="")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
