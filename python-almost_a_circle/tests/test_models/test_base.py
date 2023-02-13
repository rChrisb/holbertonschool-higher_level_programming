#!/usr/bin/python3

import unittest

from models.base import Base


class TestsBaseId(unittest.TestCase):
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
