#!/usr/bin/python3
"""
Script that create class Student that defines a student
"""


class Student():
    """
    Function that create class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that retrieves a dictionary representation
        """
        tempdict = dict()
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    tempdict[i] = self.__dict__[i]
            return tempdict
