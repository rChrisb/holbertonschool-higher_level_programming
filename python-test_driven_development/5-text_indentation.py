#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = ""
    another = ""
    for index in range(len(text)):
        if text[index - 1] in ['?', ':', '.'] and text[index] == " ":
            new_text += "\n\n"
        elif text[index - 1] in ['?', ':', '.'] and text[index] != "":
            new_text += "\n\n" + text[index]
        else:
            new_text += text[index]

    for lines in range(len(new_text.splitlines())):
        new_line = new_text.splitlines()[lines].lstrip()
        if lines == len(new_text.splitlines()) - 1:
            another += new_line
        else:
            another += new_line + "\n"

    print(another, end="")
