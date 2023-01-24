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
                if roman_string[char - 1] == "I":
                    if roman_string[char - 1] != roman_string[- 1]:
                        if roman_string[char] == "V" or roman_string[char] == "X":
                            sum -= 2

    return sum
