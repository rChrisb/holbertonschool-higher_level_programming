#!/usr/bin/python3
""" First Rectangle"""

from models.base import Base


class Rectangle(Base):
    """child of 'Base' class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def width(self, value):
        self.height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def width(self, value):
        self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def width(self, value):
        self.y = value
