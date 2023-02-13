#!/usr/bin/python3
""" First Rectangle"""

from models.base import Base


class Rectangle(Base):
    """child of 'Base' class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.integer_validator("width", self.__width)
        self.__height = height
        self.integer_validator("height", self.__height)
        self.__x = x
        self.x_y_validator("x", self.__x)
        self.__y = y
        self.x_y_validator("y", self.__y)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self.integer_validator("width", self.__width)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self.integer_validator("height", self.__height)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        self.x_y_validator("x", self.__x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        self.x_y_validator("y", self.__y)

    def integer_validator(self, name, value):
        """checks the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def x_y_validator(self, name, value):
        """checks the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for w in range(self.__height):
            print("#" * self.__width)
