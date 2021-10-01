#!/usr/bin/python3

""" class Rectangle that defines a rectangle attributes """


class Rectangle:
    """ class Rectangle with private instance attributes """

    def __init__(self, width=0, height=0):
        """init method of class Square"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        calculated_str = ""
        if self.__width != 0 and self.__height != 0:
            calculated_str += "\n".join("#" * self.__width
                for i in range(self.__height))
        return calculated_str

    def __repr__(self):
        representation_str = "Rectangle(" + str(self.__width) + ","
        representation_str += str(self.__height) + ")"
        return representation_str