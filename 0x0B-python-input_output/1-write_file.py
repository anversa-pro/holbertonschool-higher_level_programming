#!/usr/bin/python3
"""
File that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """ Function  that writes a string to a text file (UTF8)
    and returns the number of characters written
    args:
        filename (str): name of the file to be written.
        text (str): string to be written in the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
