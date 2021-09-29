#!/usr/bin/python3

"""class Square that defines a square and checks if is an integer size"""


class Square:
    """Class Square definition"""
    pass

    def __init__(self, size=0):
        """init method of class Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method that returns the current square area"""
        return (self.__size * self.__size)
