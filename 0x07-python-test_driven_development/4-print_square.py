#!/usr/bin/python3
"""
Module to print a square
Arg: Size
Return: None

"""


def print_square(size):
    """
    Module to print an sqare given a number
    Arg: Siza
    Return: None

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
