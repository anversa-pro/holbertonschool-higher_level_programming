#!/usr/bin/python3
"""
File that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string)
    args:
        my_obj (str): string to be return as JSON representation
    """
    return json.dumps(my_obj)
