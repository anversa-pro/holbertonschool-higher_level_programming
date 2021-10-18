#!/usr/bin/python3
""" Module for test the Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    "Testing suite for Base class"
    def test_create_id(self):
        """ check if new id's are set correctly """

        base0 = Base()
        self.assertEqual(base0.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base4 = Base(10)
        self.assertEqual(base4.id, 10)

        base3 = Base()
        self.assertEqual(base3.id, 3)

if __name__ == "__main__":
    unittest.main()