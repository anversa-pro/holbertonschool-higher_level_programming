#!/usr/bin/python3
""" Class to define a square """
from models.rectangle import Rectangle


class Square (Rectangle):
    """ Defines a square representation that inherits of Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        txt = "[Rectangle] ({}) {}/{} - {}"
        return txt.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        attributesList = ['id', 'size','x', 'y']
        if args is not None and len(args) > 0:
            for i, argument in enumerate(args):
                if i < len(attributesList):
                    setattr(self, attributesList[i], argument)

        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in attributesList:
                    setattr(self, key, value)
