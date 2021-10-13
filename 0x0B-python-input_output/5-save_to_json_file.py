#!/usr/bin/python3
"""
File that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation
    args:
        my_obj (str): string to be write using JSON representation
        filename (str): name of the file to be modify
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
