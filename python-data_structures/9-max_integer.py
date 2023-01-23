#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if not my_list:
        max = "None"
    else:
        for integer in range(1, len(my_list)):
            if max < my_list[integer]:
                max = my_list[integer]
    return max
