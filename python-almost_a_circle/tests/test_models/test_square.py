#!/usr/bin/python3

import unittest
import os.path
from io import StringIO
from unittest.mock import patch

from models.square import Square


class TestsSquare(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(1, 1).x, 1)
        self.assertEqual(Square(5, 2, 1).y, 1)
        with self.assertRaises(TypeError):
            Square("1", 2).size
        with self.assertRaises(TypeError):
            Square(1, "2").size
        with self.assertRaises(TypeError):
            Square(1, 5, "2").x
        # with self.assertRaises(TypeError):
        #     Square(1, 5, 7, "2").y
            
        with self.assertRaises(ValueError):
            Square(-1, 5).size
        with self.assertRaises(ValueError):
            Square(1, -5).size
        with self.assertRaises(ValueError):
            Square(1, 7, -5).size
        # with self.assertRaises(ValueError):
        #     Square(1, 8, 10, -5).size
        # with self.assertRaises(ValueError):
        #     Square(1, 0).size
        with self.assertRaises(ValueError):
            Square(0, 40).size
        
        self.assertEqual(Square(1, 1, 20, 41).id, 41)
        
    def test_area(self):
        self.assertEqual(Square(2).area(), 4)
    
    
    # def test_display_without_xy(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         Square(1, 1).display()
    #         self.assertEqual(fakeOutput.getvalue(), '#\n')

    # def test_display_with_x(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         Square(1, 1, 1).display()
    #         self.assertEqual(fakeOutput.getvalue(), ' #\n')

    # def test_display_with_xy(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         Square(1, 1, 1, 1).display()
    #         self.assertEqual(fakeOutput.getvalue(), '\n #\n')
    
    
    # def test_to_dictionary(self):
    #     self.assertEqual(Square(1, 1, 1, 1, 7).to_dictionary(), {'id': 7, 'size': 1, 'height':1, 'x': 1, 'y': 1}) 
    
    
    # def test_update(self):
    #     Square = Square(10, 10, 10, 10, 1)
    #     Square.update(id=4)
    #     self.assertEqual(Square.id, 4)
    
    # def test_create(self):
    #     Square = Square(10, 9, 8, 7, 6)
    #     r_dictionary = Square.to_dictionary()
    #     second_Square = Square.create(**r_dictionary)
    #     self.assertEqual(second_Square.id, 6)
        
    # def test_save_to_file(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         rect = Square(1, 2)
    #         rect_2 = Square(3, 3)
    #         Square.save_to_file([rect, rect_2])
    #         with open("Square.json", "r") as file:
    #             print(file.read())
    #         self.assertEqual(fakeOutput.getvalue(),'[{"id": 28, "size": 1, "height": 2, "x": 0, "y": 0}, {"id": 29, "size": 3, "height": 3, "x": 0, "y": 0}]\n')
    
    # def test_save_to_file_Empty(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         Square.save_to_file([])
    #         with open("Square.json", "r") as file:
    #             print(file.read())
    #         self.assertEqual(os.path.isfile("Square.json"), True)
    #         self.assertEqual(fakeOutput.getvalue(), '[]\n')
            
    # def test_save_to_file_creates_file(self):
    #     Square.save_to_file(None)
    #     self.assertEqual(os.path.isfile("Square.json"), True)
            
    # def test_save_to_file_None(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         Square.save_to_file(None)
    #         with open("Square.json", "r") as file:
    #             print(file.read())
    #         self.assertEqual(fakeOutput.getvalue(), '[]\n')
    #         self.assertEqual(os.path.isfile("Square.json"), True)

    # def test_save_to_file_another_None(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         Square = Square(1, 2)
    #         x = None
    #         Square.save_to_file(x)
    #         with open("Square.json", "r") as file:
    #             print(file.read())
    #         self.assertEqual(fakeOutput.getvalue(), '[]\n')
    
    # def test_load_from_file(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         r1 = Square(10, 7, 2, 8)
    #         r2 = Square(2, 4)
    #         list_Squares_input = [r1, r2]
    #         Square.save_to_file(list_Squares_input)
    #         list_Squares_output = Square.load_from_file()
    #         for rect in list_Squares_output:
    #             print("{}".format(rect))
    #         self.assertEqual(fakeOutput.getvalue(), '[Square] (24) 2/8 - 10/7\n[Square] (25) 0/0 - 2/4\n')


    
    
    # def test_str(self):
    #     self.assertEqual(Square(2, 4).__str__(), "[Square] (31) 0/0 - 2/4")