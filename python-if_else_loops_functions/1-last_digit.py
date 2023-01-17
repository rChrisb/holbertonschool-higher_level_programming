#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_ = abs(number)
l_digit = number_ % 10
if number < 0:
    l_digit = -l_digit
if (l_digit < 6) and (l_digit != 0):
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
if l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
