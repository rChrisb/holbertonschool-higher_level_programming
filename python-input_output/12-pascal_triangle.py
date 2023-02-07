#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    list = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    list[i].append(1)
                else:
                    list[i].append(list[i - 1][j] + list[i - 1][j - 1])
            elif j == i:
                list[i].append(1)
    return list
