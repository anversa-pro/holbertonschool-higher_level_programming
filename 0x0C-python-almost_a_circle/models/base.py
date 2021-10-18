#!/usr/bin/python3
""" File to define a Base Class """
import json
import os


class Base:
    """
    Defines methods to manipulate instances in this project

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor to set id's and count """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ get the string json representation from an object  """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ get the list/object from a json string representation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save a list of objects serialized in a file"""
        jlist = []
        fileName = str(cls.__name__) + ".json"
        with open(fileName, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(jlist)
            else:
                for i in range(len(list_objs)):
                    jlist.append(cls.to_dictionary(list_objs[i]))
            f.write(cls.to_json_string(jlist))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        rDummy = cls(10, 10)
        rDummy.update(**dictionary)
        return rDummy

    @classmethod
    def load_from_file(cls):
        """ return a list of instances depending on cls """
        jlistObj = []
        fileName = str(cls.__name__) + ".json"

        if os.path.exists(fileName) is False:
            return jlistObj

        with open(fileName, "r", encoding="utf-8") as f:
            jlist = cls.from_json_string(f.read())
            for i in jlist:
                    jlistObj.append(cls.create(**i))

        return jlistObj
