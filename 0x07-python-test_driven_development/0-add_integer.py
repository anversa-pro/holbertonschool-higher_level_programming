#!/usr/bin/python3
"""
Module to add 2 numbers
Arg: number a and number b
Return: Result of adding

"""


def add_integer(a, b=98):
    """
    function that validates integer args and calculate the operation
    Arg: number a and number b
    Return: Result of adding

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
