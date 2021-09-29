#!/usr/bin/python3

"""class Square that defines a square size and position"""


class Square:
    """Class Square definition"""

    def __init__(self, size=0, position=(0, 0)):
        """init method of class Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        check = all(isinstance(v, int) for v in value)
        if type(value) != tuple or len(value) != 2 or check is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for k in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
