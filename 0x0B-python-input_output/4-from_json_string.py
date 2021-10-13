#!/usr/bin/python3
"""
File that returns an object (Python data structure) 
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ 
    Function that returns an object (Python data structure) 
    represented by a JSON string:
    args:
        my_str: object to be return as JSON string
    """
    return json.loads(my_str)
