#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list2 = []
    for integer in my_list:
        my_list2.append(integer)
    my_list2[idx] = element
    return my_list2