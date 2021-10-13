#!/usr/bin/python3
"""
File that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    args:
        filename (str): name of the file to be written.
        text (str): string to be append in the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
