#!/usr/bin/python3
""" File to define a Rectangle Class """
from models.base import Base


class Rectangle (Base):
    """
    Defines methods of a rectangle that inherits of Base class

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor to set instance attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ return the instance width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the instance width if validate """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ return the instance height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the instance height if validate """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ return the instance x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the instance x if validate """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ return the instance y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the instance y if validate """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate a rectangle area (w * h) and return it """
        return (self.width * self.height)

    def display(self):
        """ prints a representation of a square by consecutive # """
        print('\n' * self.y, end='')
        for counter in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width, end='')
            if counter + 1 < self.height:
                print()
        print()

    def __str__(self):
        """ Modify the stdr output with a specific format """
        txt = "[Rectangle] ({}) {}/{} - {}/{}"
        return txt.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Modify instance values according args or kwargs input """
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
        """ Returns the dictionary representation of a Rectangle """
        traitList = ['x', 'y', 'id', 'height', 'width']
        printDictionary = {}
        for trait in traitList:
            printDictionary[trait] = getattr(self, trait)
        return printDictionary
