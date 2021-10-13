#!/usr/bin/python3
"""
File that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    args:
        filename: JSON file to create an Object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
