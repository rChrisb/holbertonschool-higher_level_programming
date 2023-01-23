#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = []
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        x.append(tuple_a[0] + tuple_b[0])
        x.append(tuple_a[1] + tuple_b[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        x.append(tuple_a[0] + tuple_b[0])
        x.append(tuple_b[1])
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        x.append(tuple_a[0] + tuple_b[0])
        x.append(tuple_a[1])
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        x.append(tuple_a[0])
        x.append(tuple_a[1])
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        x.append(tuple_b[0])
        x.append(tuple_b[1])
    return tuple(x)
