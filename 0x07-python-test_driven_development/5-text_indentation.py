#!/usr/bin/python3
"""
Defines a text-indentation function.
Arg: String
Return: None

"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    Deletes spaces after characters

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    iterator = 0
    while iterator < len(text) and text[iterator] == ' ':
        iterator += 1

    while iterator < len(text):
        print(text[iterator], end="")
        if text[iterator] == "\n" or text[iterator] in ".?:":
            if text[iterator] in ".?:":
                print("\n")
            iterator += 1
            while iterator < len(text) and text[iterator] == ' ':
                iterator += 1
            continue
        iterator += 1
