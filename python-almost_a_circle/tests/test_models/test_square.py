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
    
    
    def test_to_dictionary(self):
        self.assertEqual(Square(1, 1, 1, 7).to_dictionary(), {'id': 7, 'size': 1, 'x': 1, 'y': 1}) 
    
    
    def test_update(self):
        square = Square(10, 10, 10, 1)
        square.update(id=4)
        self.assertEqual(square.id, 4)
    
    def test_create(self):
        square = Square(10, 9, 8, 6)
        r_dictionary = square.to_dictionary()
        second_square = square.create(**r_dictionary)
        self.assertEqual(second_square.id, 6)
        
    def test_save_to_file(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            square = Square(1, 0, 0, 33)
            square_2 = Square(3, 0, 0, 57)
            Square.save_to_file([square, square_2])
            with open("Square.json", "r") as file:
                print(file.read())
            self.assertEqual(fakeOutput.getvalue(),'[{"id": 33, "size": 1, "x": 0, "y": 0}, {"id": 57, "size": 3, "x": 0, "y": 0}]\n')
    
    def test_save_to_file_Empty(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Square.save_to_file([])
            with open("Square.json", "r") as file:
                print(file.read())
            self.assertEqual(os.path.isfile("Square.json"), True)
            self.assertEqual(fakeOutput.getvalue(), '[]\n')
            os.remove("Rectangle.json")
            
    def test_save_to_file_creates_file(self):
        Square.save_to_file(None)
        self.assertEqual(os.path.isfile("Square.json"), True)
            
    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")

    # def test_save_to_file_another_None(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         square = Square(1)
    #         x = None
    #         square.save_to_file(x)
    #         with open("Square.json", "r") as file:
    #             print(file.read())
    #         self.assertEqual(fakeOutput.getvalue(), '[]\n')
    
    def test_load_from_file(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            s1 = Square(10, 7, 2, 88)
            s2 = Square(2, 0, 0, 99)
            list_Squares_input = [s1, s2]
            Square.save_to_file(list_Squares_input)
            list_Squares_output = Square.load_from_file()
            for rect in list_Squares_output:
                print("{}".format(rect))
            self.assertEqual(fakeOutput.getvalue(), '[Square] (88) 7/2 - 10\n[Square] (99) 0/0 - 2\n')

    
    def test_str(self):
        square = Square(4, 0, 0, 2)
        self.assertEqual(square.__str__(), "[Square] (2) 0/0 - 4")