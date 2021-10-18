#!/usr/bin/python3
""" Class to define a rectangle """
from models.base import Base


class Rectangle (Base):
    """ Defines a rectangle representation that inherits of Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate a rectangle area (w * h) and return it """
        return (self.width * self.height)

    def display(self):
        """ prints a representation of the square by # """
        print('\n' * self.y, end='')
        for counter in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width, end='')
            if counter + 1 < self.height:
                print()
        print()

    def __str__(self):
        txt = "[Rectangle] ({}) {}/{} - {}/{}"
        return txt.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        attributesList = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) > 0:
            for i, argument in enumerate(args):
                if i < len(attributesList):
                    setattr(self, attributesList[i], argument)

        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in attributesList:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ that returns the dictionary representation of a Rectangle """
        traitList = ['x', 'y', 'id', 'height', 'width']
        printDictionary = {}
        for trait in traitList:
            printDictionary[trait] = getattr(self, trait)
        return printDictionary
