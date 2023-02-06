#!/usr/bin/python3
"""Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    if type(my_obj) is set:
        raise PermissionError("13", f"Permission denied: '{filename}'")
    json_string = json.dumps(my_obj)
    with open(filename, "a") as file:
        file.write(json_string)
