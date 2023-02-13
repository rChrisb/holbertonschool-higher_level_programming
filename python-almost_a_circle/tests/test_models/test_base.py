#!/usr/bin/python3

import unittest

from models.base import Base


class TestsBaseId(unittest.TestCase):
    def test_base(self):
        first_base = Base()
        third_base = Base(89)
        second_base = Base()
        fourth_base = Base()

        self.assertEqual(first_base.id, 1)
        self.assertEqual(second_base.id, 2)
        self.assertEqual(third_base.id, 89)
        self.assertEqual(fourth_base.id, 3)


if __name__ == '__main__':
    unittest.main()
