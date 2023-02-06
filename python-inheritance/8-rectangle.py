#!/usr/bin/python3
"""Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)
