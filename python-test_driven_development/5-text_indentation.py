#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = ""
    for index in range(len(text)):
        if text[index - 1] in ['?', ':', '.'] and text[index] == " ":
            new_text += "\n\n"
        elif text[index - 1] in ['?', ':', '.'] and text[index] != "":
            new_text += "\n\n" + text[index]
        else:
            new_text += text[index]
    print(new_text, end="")
