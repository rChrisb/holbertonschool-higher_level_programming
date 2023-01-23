#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    total = 0
    for number in new_list:
        total += number
    return total
