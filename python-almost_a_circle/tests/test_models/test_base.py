#!/usr/bin/python3

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestsBase(unittest.TestCase):
    def test_base(self):
        # first_base = Base()
        # third_base = Base(89)
        # second_base = Base()
        # fourth_base = Base()

        # self.assertEqual(first_base.id, 1)
        # self.assertEqual(second_base.id, 2)
        # self.assertEqual(third_base.id, 89)
        # self.assertEqual(fourth_base.id, 3)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(89).id, 89)
        self.assertNotEqual(Base().id, 90)
        self.assertEqual(Base().id, 4)

    def test_id_incremental(self):
        self.assertEqual(Base().id, 5)
        self.assertEqual(Base().id, 6)

    def test_not_none(self):
        self.assertNotEqual(Base().id, None)
    
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
    
    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])

    # def test_test(self):
    #     if (self.__class__.__name__ != "Base"):
    #         Base.save_to_file(None)
    #         with open(f"{type(self)}.json", "r") as file:  error: No such file or directory: "<class 'test_models.test_base.TestsBase'>.json
    #             self.assertEqual(file.read(), "[]")
        
    # def test_save_to_file_None_square(self):
    #     Square.save_to_file(None)
    #     with open("Square.json", "r") as file:
    #         self.assertEqual(file.read(), '[]')
    

    
    # def test_save_to_file_None_rectangle(self):
    #     Rectangle.save_to_file(None)
    #     with open("Rectangle.json", "r") as file:
    #         self.assertEqual(file.read(), '[]')
