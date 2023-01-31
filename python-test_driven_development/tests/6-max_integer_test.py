#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([7, 2, 3]), 7)
        self.assertEqual(max_integer([1, 10, 3]), 10)
        self.assertEqual(max_integer([10]), 10)
        self.assertNotEqual(max_integer([1, 12, 3]), 3)
        self.assertNotEqual(max_integer([-1, -2, -3]), 3)
        self.assertNotEqual(max_integer([1, 12, -3]), 3)
        self.assertNotEqual(max_integer([]), 3)


if __name__ == '__main__':
    unittest.main()
