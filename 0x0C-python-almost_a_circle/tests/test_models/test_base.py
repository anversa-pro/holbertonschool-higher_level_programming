#!/usr/bin/python3
""" Module for test the Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.case import skip
from contextlib import redirect_stdout
import io
import os
import json


class TestBase(unittest.TestCase):
    "Testing suite for Base class"
    def setUp(self):
        """reset the id objects number"""
        Rectangle.resetNumber()

    def test_create_id(self):
        """ check if new id's are set correctly """
        base0 = Base()
        self.assertEqual(base0.id, 1)
        base1 = Base()
        self.assertEqual(base1.id, 2)
        base2 = Base(10)
        self.assertEqual(base2.id, 10)
        base3 = Base()
        self.assertEqual(base3.id, 3)

    def test_to_json_string(self):
        """ check if return the correct json string from a list of dicts """
        base0 = Base(1)
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string(None), '[]')
 
    def test_from_json_string(self):
        """ check if return the correct json string from a list of dicts """
        string = '{"a": 1, "b": 2}'
        dictionary = json.loads(string)
        base = Base(12)
        self.assertEqual(base.from_json_string(string), dictionary)
        self.assertEqual(base.from_json_string(None), [])
        self.assertEqual(base.from_json_string('[]'), [])

    def test_save_to_file(self):
        """ check if save correctly the serialized objects in a file """
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect2 = Rectangle(6, 7)
        rect2.id = 8
        rect1.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            response = json.loads(file.read())
        list_dicts = [{'y': 4, 'x': 3, 'id': 5, 'width': 1, 'height': 2},
                      {'y': 0, 'x': 0, 'id': 8, 'width': 6, 'height': 7}]
        self.assertEqual(response, list_dicts)

        sqr1 = Square(1, 2, 3, 4)
        sqr2 = Square(5)
        sqr2.id = 6
        sqr2.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as file:
            response = json.loads(file.read())
        list_dicts = [{'y': 3, 'x': 2, 'id': 4, 'size': 1},
                      {'y': 0, 'x': 0, 'id': 6, 'size': 5}]
        self.assertEqual(response, list_dicts)

        rect1.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            response = json.loads(file.read())
        list_dicts = []
        self.assertEqual(response, list_dicts)

        sqr2.save_to_file(None)
        with open("Square.json", "r") as file:
            response = json.loads(file.read())
        list_dicts = []
        self.assertEqual(response, list_dicts)

    def test_create(self):
        """ create instances of the object with the values in the diction.. """
        dictionary = {'y': 5, 'x': 4, 'id': 1, 'width': 2, 'height': 3}
        instance = Rectangle.create(**dictionary)
        self.assertEqual(type(instance), Rectangle)
        self.assertEqual(instance.__str__(), "[Rectangle] (1) 4/5 - 2/3")

        dictionary = {'y': 5, 'x': 4, 'id': 1, 'size': 2}
        instance = Square.create(**dictionary)
        self.assertEqual(type(instance), Square)
        self.assertEqual(instance.__str__(), "[Square] (1) 4/5 - 2")

    def test_load_from_file(self):
        """ checks if create an array of the instances """
        file_name = "Rectangle.json"
        try:
            os.remove(file_name)
        except:
            pass
        list_of_instances = Rectangle.load_from_file()
        self.assertEqual(type(list_of_instances), list)
        self.assertEqual(len(list_of_instances), 0)

        list_dicts = [{'y': 4, 'x': 3, 'id': 5, 'width': 1, 'height': 2},
                      {'y': 0, 'x': 0, 'id': 8, 'width': 6, 'height': 7}]
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(Rectangle.to_json_string(list_dicts))
        list_of_instances = Rectangle.load_from_file()
        self.assertEqual(type(list_of_instances), list)
        self.assertEqual(len(list_of_instances), 2)
        self.assertEqual(list_of_instances[0].__str__(),
                         "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(list_of_instances[1].__str__(),
                         "[Rectangle] (8) 0/0 - 6/7")

        file_name = "Square.json"
        try:
            os.remove(file_name)
        except:
            pass
        list_of_instances = Square.load_from_file()
        self.assertEqual(type(list_of_instances), list)
        self.assertEqual(len(list_of_instances), 0)

        list_dicts = [{'y': 3, 'x': 2, 'id': 4, 'size': 1},
                      {'y': 0, 'x': 0, 'id': 6, 'size': 5}]
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(Square.to_json_string(list_dicts))
        list_of_instances = Square.load_from_file()
        self.assertEqual(type(list_of_instances), list)
        self.assertEqual(len(list_of_instances), 2)
        self.assertEqual(
            list_of_instances[0].__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(
            list_of_instances[1].__str__(), "[Square] (6) 0/0 - 5")

if __name__ == "__main__":
    unittest.main()