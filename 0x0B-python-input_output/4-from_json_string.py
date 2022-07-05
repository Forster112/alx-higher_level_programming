#!/usr/bin/python3
import json
"""json module"""


def from_json_string(my_str):
    """converts a json string to python"""
    return json.load(my_str)
