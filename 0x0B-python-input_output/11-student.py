#!/usr/bin/python3

"""Class that defines Student"""


class Student:
    """Class that defines Student"""
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

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]
