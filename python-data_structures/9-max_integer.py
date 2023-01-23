#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max = my_list[0]
        for integer in range(1, len(my_list)):
            if max < my_list[integer]:
                max = my_list[integer]
    return max
