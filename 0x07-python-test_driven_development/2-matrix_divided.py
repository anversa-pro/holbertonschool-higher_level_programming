#!/usr/bin/python3
"""
Module to divide a list by a number
Arg: Matrix & divisor
Return: New list divided

"""


def matrix_divided(matrix, div):
    """
    Function to verify args and do the operation
    Arg: Matrix & divisor
    Return: New list divided

    """

    TypeErr_str = "matrix must be a matrix (list of lists) of integers/floats"

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all((isinstance(i, int) or (isinstance(i, float)))
               for i in [j for row in matrix for j in row]):
                    raise TypeError(TypeErr_str)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("ZeroDivisionError")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
