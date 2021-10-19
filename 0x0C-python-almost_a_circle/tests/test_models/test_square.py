#!/usr/bin/python3
""" Module for test the Square class """
import unittest
from models.square import Square
from models.base import Base
from unittest.case import skip
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    "Testing suite for Square class"
    def setUp(self):
        """reset the id objects number"""
        Base.resetNumber()

    def test_create_id(self):
        """ check if new id's are set correctly """
        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        s1 = Square(3)
        self.assertEqual(s1.id, 2)
        s2 = Square(5, 7, 0, 0)
        self.assertEqual(s2.id, 0)
        s3 = Square(6, 8)
        self.assertEqual(s3.id, 3)

    def test_dimensions(self):
        """ check if w & h dimensions are validate """

        rDim = Square(5)
        self.assertEqual(rDim.width, 5)
        self.assertEqual(rDim.height, 5)

        rDim.width = 10
        rDim.height = 3
        self.assertEqual(rDim.width, 10)
        self.assertEqual(rDim.height, 3)

        rDim.width = 0x0F
        rDim.height = 0x0F
        self.assertEqual(rDim.width, 15)
        self.assertEqual(rDim.height, 15)

        self.assertRaises(TypeError, Square, 'Cinco', 10)
        self.assertRaises(TypeError, Square, 10, '5')

        self.assertRaises(TypeError, Square, None, 10)
        self.assertRaises(TypeError, Square, 10, None)

        self.assertRaises(TypeError, Square, True, 10)
        self.assertRaises(TypeError, Square, 10, True)

        self.assertRaises(ValueError, Square, -5, 10)
        self.assertRaises(ValueError, Square, 5, -10)

        self.assertRaises(ValueError, Square, 0)

    def test_str(self):
        """ check if the printable representation is correct """

        s0 = Square(4, 2, 1, 12)
        self.assertEqual(str(s0), '[Square] (12) 2/1 - 4')
        s1 = Square(5)
        s1.id = 16
        self.assertEqual(str(s1), '[Square] (16) 0/0 - 5')

    def test_update_args(self):
        """ check the update function with 'no-keyword' arguments """

        rUpdateArg = Square(5)

        rUpdateArg.update(6)
        self.assertEqual(rUpdateArg.id, 6)

        rUpdateArg.update(10, 5)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 5 * 5)

        rUpdateArg.update(10, 10, 10)
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        self.assertEqual(rUpdateArg.x, 10)

        rUpdateArg.update(10, 10, 10, 10)
        self.assertEqual(rUpdateArg.y, 10)

        rUpdateArg.update(20, 21, 22, 23, 24, 25)
        self.assertEqual(rUpdateArg.id, 20)
        self.assertEqual(rUpdateArg.area(), 21 * 21)
        self.assertEqual(rUpdateArg.x, 22)
        self.assertEqual(rUpdateArg.y, 23)

        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        self.assertEqual(rUpdateArg.x, 15)
        self.assertEqual(rUpdateArg.y, 20)

        rUpdateArg.update('A', 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 'A')
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        self.assertEqual(rUpdateArg.x, 15)
        self.assertEqual(rUpdateArg.y, 20)

        self.assertRaises(TypeError, rUpdateArg.update(), 6, "3", 10, 19)
        self.assertRaises(TypeError, rUpdateArg.update(), 10, 5, 5, None)

        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 0, 5, 0)

    def test_update_kwargs(self):
        """ check update function with 'key-worded' argument """

        rUpdateKarg = Square(5)

        rUpdateKarg.update(id=6)
        self.assertEqual(rUpdateKarg.id, 6)

        rUpdateKarg.update(id=10, size=5)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 5 * 5)

        rUpdateKarg.update(id=10, size=7)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 7)

        rUpdateKarg.update(id=10, size=7, x=9)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 7)
        self.assertEqual(rUpdateKarg.x, 9)

        rUpdateKarg.update(y=14, id=6, x=19, size=3)
        self.assertEqual(rUpdateKarg.id, 6)
        self.assertEqual(rUpdateKarg.area(), 9)
        self.assertEqual(rUpdateKarg.x, 19)
        self.assertEqual(rUpdateKarg.y, 14)

    def test_to_dict(self):
        """ check if to_dictionary returns the dict correctly """
        s0 = Square(4, 8, 3, 12)
        expect_out = {'id': 12, 'size': 4, 'x': 8, 'y': 3}
        self.assertEqual(s0.to_dictionary(), expect_out)


if __name__ == "__main__":
    unittest.main()