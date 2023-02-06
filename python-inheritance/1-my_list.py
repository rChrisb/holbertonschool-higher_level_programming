#!/usr/bin/python3
"""My list"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
        return sorted(self)
