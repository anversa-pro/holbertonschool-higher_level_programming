#!/usr/bin/python3
"""
Module to print a name
Arg: first & last name
Return: None

"""


def say_my_name(first_name, last_name=""):
    """
    Module to find print a name
    Arg: List
    Return: Max integer in a given list

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
