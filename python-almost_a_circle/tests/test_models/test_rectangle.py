#!/usr/bin/python3

import unittest

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
    
    def test_str(self):
        self.assertEqual(Rectangle(2, 4).__str__(), "[Rectangle] (23) 0/0 - 2/4")
    
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