#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    times = 0
    skip = 0
    if x == 0:
        print()
    try:
        while times < x:
            if type(my_list[times]) is not int:
                times += 1
                skip += 1
            if times == x - 1:
                print("{:d}".format(my_list[times]))
            else:
                print("{:d}".format(my_list[times]), end="")
            times += 1
        return times - skip
    except IndexError:
        if times < x:
            raise
        print()
        return times - skip
