#!/usr/bin/python3

for i in range(0, 9):
    for x in range(0, 10):
        if (i == 1 and x == 0) or (i == 2 and x == 0) or (i == 2 and x == 1):
            continue
        if (i == 3 and x == 0) or (i == 3 and x == 1) or (i == 3 and x == 2):
            continue
        if (i == 4 and x == 0) or (i == 4 and x == 1) or (i == 4 and x == 2):
            continue
        if (i == 4 and x == 3) or (i == 4 and x == 4):
            continue
        if (i == 5 and x == 0) or (i == 5 and x == 1) or (i == 5 and x == 2):
            continue
        if (i == 5 and x == 3) or (i == 5 and x == 4) or (i == 6 and x == 0):
            continue
        if (i == 6 and x == 1) or (i == 6 and x == 2) or (i == 6 and x == 3):
            continue
        if (i == 6 and x == 4) or (i == 6 and x == 5) or (i == 7 and x == 0):
            continue
        if (i == 7 and x == 1) or (i == 7 and x == 2) or (i == 7 and x == 3):
            continue
        if (i == 7 and x == 4) or (i == 7 and x == 5) or (i == 7 and x == 6):
            continue
        if (i == 8 and x == 0) or (i == 8 and x == 1) or (i == 8 and x == 2):
            continue
        if (i == 8 and x == 3) or (i == 8 and x == 4) or (i == 8 and x == 5):
            continue
        if (i == 8 and x == 6) or (i == 8 and x == 7):
            continue
        if i == 8 and x == 9:
            print(f"{i}{x}")
        elif i != x:
            print(f"{i}{x}", end=', ')
