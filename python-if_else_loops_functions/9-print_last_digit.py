#!/usr/bin/python3
def print_last_digit(number):
    number_ = abs(number)
    l_digit = number_ % 10
    print(l_digit, end='')
    return l_digit
