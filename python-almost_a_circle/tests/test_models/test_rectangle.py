#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle


class TestsRectangle(unittest.TestCase):
    def test_instanciation(self):
        self.assertEqual(Rectangle(1, 2).width, 1)