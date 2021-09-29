#!/usr/bin/python3

"""class Square that defines a square and checks if is an integer size"""


class Square:
    """Class Square definition"""
    pass

    def __init__(self, size=0):
        """init method of class Square"""
        self.size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        return (self.size * self.size)
