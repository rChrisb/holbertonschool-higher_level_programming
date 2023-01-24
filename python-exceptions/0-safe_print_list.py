#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    times = 0
    if x == 0:
        print()
    try:
        while times < x:
            if times == x - 1:
                print("{}".format(my_list[times]))
            else:
                print("{}".format(my_list[times]), end="")
            times += 1
    except IndexError:
        print()
        return times

    return times
