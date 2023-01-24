#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    if roman_string is None:
        return sum
    for char in range(len(roman_string)):
        for (letter, value) in dic.items():
            if roman_string[char] is letter:
                sum += value
                if roman_string[char - 1] is "I":
                    if roman_string[char] is not "I":
                        sum -= 2
                    else:
                        sum += 2
    return sum
