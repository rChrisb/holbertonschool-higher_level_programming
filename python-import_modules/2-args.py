#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 == 0:
        print("{}".format(len(argv) - 1), end=' arguments.\n')
    if len(argv) - 1 == 1:
        print("{}".format(len(argv) - 1), end=' argument:\n')
    print("{}".format(len(argv) - 1), end=' arguments:\n')
if len(argv) != 0:
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
