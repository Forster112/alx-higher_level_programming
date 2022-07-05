#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
"""adds argument to a python list and save to a file"""
new_list = []
filename = "add_item.json"

for i in argv[1:]:
    new_list.append(i)
save_to_json_file(new_list, filename)
load_from_json_file(filename)
