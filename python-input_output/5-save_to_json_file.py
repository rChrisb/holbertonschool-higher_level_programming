#!/usr/bin/python3
"""Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    # json_string = json.dumps(my_obj)
    # with open(filename, "w") as file:
    #     file.write(json_string)
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
    file.closed
