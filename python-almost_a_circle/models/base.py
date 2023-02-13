#!/usr/bin/python3
""" Base class"""

import json


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """turns object to JSON string"""
        if list_dictionaries == {} or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        for obj in list_objs:
            new_list.append(cls.to_dictionary(obj))
        content_json = cls.to_json_string(new_list)
        with open(f"{cls.__name__}.json", "w") as json_file:
            json_file.write(content_json)
