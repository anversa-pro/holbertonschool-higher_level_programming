#!/usr/bin/python3
""" File to define a Square Class """
from models.rectangle import Rectangle


class Square (Rectangle):
    """
    Defines methods of a square that inherits of Rectangle class

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor to set instance attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return the instance size value """
        return self.width

    @size.setter
    def size(self, value):
        """ set the instances w & h if validate """
        self.width = value
        self.height = value

    def __str__(self):
        """ Modify the stdr output with a specific format """
        txt = "[{}] ({}) {}/{} - {}"
        return txt.format(type(self).__name__, self.id,
                          self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Modify instance values according args or kwargs input """
        attributesList = ['id', 'size', 'x', 'y']
        if args is not None and len(args) > 0:
            for i, argument in enumerate(args):
                if i < len(attributesList):
                    setattr(self, attributesList[i], argument)

        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in attributesList:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        traitList = ['id', 'x', 'size', 'y']
        printDictionary = {}
        for trait in traitList:
            printDictionary[trait] = getattr(self, trait)
        return printDictionary
