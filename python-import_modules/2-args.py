#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format(len(argv) - 1), end=' arguments.\n')
if len(argv) != 0:
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
