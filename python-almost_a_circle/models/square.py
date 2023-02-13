#!/usr/bin/python3
"""And now, the Square!"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.integer_validator("width", value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} -\
 {self.height}"
