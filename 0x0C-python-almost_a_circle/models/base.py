#!/usr/bin/python3
""" FIRST CLASS """
import json

class Base:
    "Base of all other classes in this project"
    __nb_objects = 0

    def __init__(self, id=None):
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
        """ obtains the list/object from a json string representation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save a list of objects serialized in a csv file """

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

    @classmethod
    def load_from_file(cls):
        """ return a list of instances depending on cls """
