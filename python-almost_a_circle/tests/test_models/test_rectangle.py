#!/usr/bin/python3

import unittest

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