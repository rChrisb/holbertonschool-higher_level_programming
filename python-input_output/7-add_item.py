#!/usr/bin/python3
"""Load, add, save"""


import json
from sys import argv
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json") is False:
    save_to_json_file([], "add_item.json")

content = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    content.append(argv[i])
save_to_json_file(content, "add_item.json")
