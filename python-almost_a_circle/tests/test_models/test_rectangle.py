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
        