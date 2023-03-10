#!/usr/bin/python3

import unittest
import os.path
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle



class TestsRectangle(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(Rectangle(1, 2).width, 1)
        with self.assertRaises(TypeError):
            Rectangle("1", 2).width
        with self.assertRaises(TypeError):
            Rectangle(1, "2").width
        with self.assertRaises(TypeError):
            Rectangle(1, 5, "2").x
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 7, "2").y
            
        with self.assertRaises(ValueError):
            Rectangle(-1, 5).width
        with self.assertRaises(ValueError):
            Rectangle(1, -5).width
        with self.assertRaises(ValueError):
            Rectangle(1, 7, -5).width
        with self.assertRaises(ValueError):
            Rectangle(1, 8, 10, -5).width
        with self.assertRaises(ValueError):
            Rectangle(1, 0).width
        with self.assertRaises(ValueError):
            Rectangle(0, 40).width
        
        self.assertEqual(Rectangle(1, 1, 1, 20, 41).id, 41)
        
    def test_area(self):
        self.assertEqual(Rectangle(2, 5).area(), 10)
    
    
    def test_display_without_xy(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Rectangle(1, 1).display()
            self.assertEqual(fakeOutput.getvalue(), '#\n')

    def test_display_with_x(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Rectangle(1, 1, 1).display()
            self.assertEqual(fakeOutput.getvalue(), ' #\n')

    def test_display_with_xy(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Rectangle(1, 1, 1, 1).display()
            self.assertEqual(fakeOutput.getvalue(), '\n #\n')
    
    
    def test_to_dictionary(self):
        self.assertEqual(Rectangle(1, 1, 1, 1, 7).to_dictionary(), {'id': 7, 'width': 1, 'height':1, 'x': 1, 'y': 1}) 
    
    
    def test_update(self):
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(id=4)
        self.assertEqual(rectangle.id, 4)
    
    def test_create(self):
        rectangle = Rectangle(10, 9, 8, 7, 6)
        r_dictionary = rectangle.to_dictionary()
        second_rectangle = Rectangle.create(**r_dictionary)
        self.assertEqual(second_rectangle.id, 6)
        
    def test_save_to_file(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            rect = Rectangle(1, 2, 0, 0 , 300)
            rect_2 = Rectangle(3, 3, 0, 0 , 301)
            Rectangle.save_to_file([rect, rect_2])
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(fakeOutput.getvalue(),'[{"id": 300, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 301, "width": 3, "height": 3, "x": 0, "y": 0}]\n')
    
    def test_save_to_file_Empty(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Rectangle.save_to_file([])
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(os.path.isfile("Rectangle.json"), True)
            self.assertEqual(fakeOutput.getvalue(), '[]\n')
            os.remove("Rectangle.json")
            
    def test_save_to_file_creates_file(self):
        Rectangle.save_to_file(None)
        self.assertEqual(os.path.isfile("Rectangle.json"), True)
            
    def test_save_to_file_None(self):
        # with patch('sys.stdout', new=StringIO()) as fakeOutput:
        #     Rectangle.save_to_file(None)
        #     with open("Rectangle.json", "r") as file:
        #         print(file.read())
        #     self.assertEqual(fakeOutput.getvalue(), '[]\n')
        #     self.assertEqual(os.path.isfile("Rectangle.json"), True)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    # def test_save_to_file_another_None(self):
    #     with patch('sys.stdout', new=StringIO()) as fakeOutput:
    #         rectangle = Rectangle(1, 2)
    #         x = None
    #         rectangle.save_to_file(x)
    #         with open("Rectangle.json", "r") as file:
    #             print(file.read())
    #         self.assertEqual(fakeOutput.getvalue(), '[]\n')
    
    def test_load_from_file(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1 = Rectangle(10, 7, 2, 8, 200)
            r2 = Rectangle(2, 4, 0, 0, 201)
            list_rectangles_input = [r1, r2]
            Rectangle.save_to_file(list_rectangles_input)
            list_rectangles_output = Rectangle.load_from_file()
            for rect in list_rectangles_output:
                print("{}".format(rect))
            self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (200) 2/8 - 10/7\n[Rectangle] (201) 0/0 - 2/4\n')


    
    
    def test_str(self):
        self.assertEqual(Rectangle(2, 4, 0, 0, 100).__str__(), "[Rectangle] (100) 0/0 - 2/4")