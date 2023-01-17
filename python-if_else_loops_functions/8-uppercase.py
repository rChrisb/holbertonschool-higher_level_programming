#!/usr/bin/python3
def uppercase(str):
    result = ''
    for letter in str:
        if ord(letter) <= 122 and ord(letter) >= 97:
            result += chr(ord(letter) - 32)
        elif ord(letter) < 97 or ord(letter) > 122:
            result += letter
    print(result)
