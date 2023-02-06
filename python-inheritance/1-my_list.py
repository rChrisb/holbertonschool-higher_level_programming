#!/usr/bin/python3
"""My list"""


class MyList(list):
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
