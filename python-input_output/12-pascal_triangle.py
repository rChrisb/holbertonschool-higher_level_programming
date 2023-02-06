#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    list = []
    if n <= 0:
        return list
    list.append([1])
    list.append([1, 1])
    list.append([1, 2, 1])
    return list
