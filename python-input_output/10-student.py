#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = vars(self)
        if attrs is not None:
            return dict(filter(lambda pair: pair[0] in attrs, d.items()))
        return d
