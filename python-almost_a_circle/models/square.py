#!/usr/bin/python3
"""And now, the Square!"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.integer_validator("width", value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} -\
 {self.width}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        if len(args) >= 1:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return updated dictionary for Square instance"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
