#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    if roman_string is None or type(roman_string) is not str:
        return sum
    for c in range(len(roman_string)):
        for (letter, value) in dic.items():
            if roman_string[c] is letter:
                sum += value
                if roman_string[c - 1] == "I":
                    if roman_string[c - 1] != roman_string[- 1]:
                        if roman_string[c] == "V" or roman_string[c] == "X":
                            sum -= 2

    return sum
