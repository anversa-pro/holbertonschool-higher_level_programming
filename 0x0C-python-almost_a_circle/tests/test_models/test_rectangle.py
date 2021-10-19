#!/usr/bin/python3
""" Module for test the Rectangle class """
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.case import skip
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Testing suite for Rectangle class"""

    def setUp(self):
        """reset the id objects number"""
        Base.resetNumber()

    def test_create_id(self):
        """ check if new id's are set correctly """
        r0 = Rectangle(1, 3)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(5, 7, 0, 0, 10)
        self.assertEqual(r2.id, 10)
        r3 = Rectangle(6, 8)
        self.assertEqual(r3.id, 3)

    def test_dimensions(self):
        """ check if w & h dimensions are validate """

        rDim = Rectangle(2, 8)
        self.assertEqual(rDim.width, 2)
        self.assertEqual(rDim.height, 8)

        rDim.width = 10
        rDim.height = 3
        self.assertEqual(rDim.width, 10)
        self.assertEqual(rDim.height, 3)

        rDim.width = 0x0F
        rDim.height = 0x0F
        self.assertEqual(rDim.width, 15)
        self.assertEqual(rDim.height, 15)

        self.assertRaises(TypeError, Rectangle, 'Cinco', 10)
        self.assertRaises(TypeError, Rectangle, 10, '5')

        self.assertRaises(TypeError, Rectangle, None, 10)
        self.assertRaises(TypeError, Rectangle, 10, None)

        self.assertRaises(TypeError, Rectangle, True, 10)
        self.assertRaises(TypeError, Rectangle, 10, True)

        self.assertRaises(ValueError, Rectangle, -5, 10)
        self.assertRaises(ValueError, Rectangle, 5, -10)

        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_position(self):
        """ check if the position x y y are validates and sets correctly """

        r0 = Rectangle(10, 2)
        self.assertEqual(r0.x, 0)
        self.assertEqual(r0.y, 0)

        r0 = Rectangle(10, 2, 10)
        self.assertEqual(r0.x, 10)
        self.assertEqual(r0.y, 0)

        r0 = Rectangle(10, 2, 10, 2)
        self.assertEqual(r0.x, 10)
        self.assertEqual(r0.y, 2)

        r0.x = 13
        r0.y = 8
        self.assertEqual(r0.x, 13)
        self.assertEqual(r0.y, 8)

        self.assertRaises(TypeError, Rectangle, 10, 10, "e", 10)
        self.assertRaises(TypeError, Rectangle, 10, 10, 0, "10")

        self.assertRaises(ValueError, Rectangle, 10, 10, -8, 10)
        self.assertRaises(ValueError, Rectangle, 10, 10, 10, -1)

    def test_area(self):
        """ check if the area is calculate correctly """

        r0 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r0.area(), 6)
        r0.width = 1
        self.assertEqual(r0.area(), 3)
        r0.height = 1
        self.assertEqual(r0.area(), 1)

    def test_str(self):
        """ check if the printable representation is correct """

        r0 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r0), '[Rectangle] (12) 2/1 - 4/6')
        r1 = Rectangle(5, 5)
        r1.id = 16
        self.assertEqual(str(r1), '[Rectangle] (16) 0/0 - 5/5')

    def test_display(self):
        """ check if the display function shows the right size of rectangle """
        rDisplay = Rectangle(1, 1)
        expected_out = '#\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rDisplay.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

        rDisplay.width = 2
        rDisplay.height = 3
        expected_out = '##\n##\n##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rDisplay.display()
            self.assertEqual(fake_out.getvalue(), expected_out)
        rDisplay.x = 1
        rDisplay.y = 3
        expected_out = '\n\n\n ##\n ##\n ##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rDisplay.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

        rDisplay.x = 1
        rDisplay.y = 0
        expected_out = ' ##\n ##\n ##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rDisplay.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

        rDisplay.x = 4
        rDisplay.y = 1
        rDisplay.width = 1
        rDisplay.height = 1
        expected_out = '\n    #\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rDisplay.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

    def test_update_args(self):
        """ check the update function with 'no-keyword' arguments """

        rUpdateArg = Rectangle(1, 2)

        rUpdateArg.update(6)
        self.assertEqual(rUpdateArg.id, 6)

        rUpdateArg.update(10, 5)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 5 * 2)

        rUpdateArg.update(10, 10, 10)
        self.assertEqual(rUpdateArg.area(), 10 * 10)

        rUpdateArg.update(10, 10, 10, 10)
        self.assertEqual(rUpdateArg.x, 10)

        rUpdateArg.update(10, 10, 10, 10, 10)
        self.assertEqual(rUpdateArg.y, 10)

        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)

        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)

        rUpdateArg.update('A', 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 'A')
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)

        self.assertRaises(TypeError, rUpdateArg.update(), 6, "3", 10, 19, 14)
        self.assertRaises(TypeError, rUpdateArg.update(), 10, 5, 5, None, 0)

        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 5, 0, 0, 0)

        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 0, 5, 0, 0)

    def test_update_kwargs(self):
        """ check update function with 'key-worded' argument """

        rUpdateKarg = Rectangle(1, 2)

        rUpdateKarg.update(id=6)
        self.assertEqual(rUpdateKarg.id, 6)

        rUpdateKarg.update(id=10, width=5)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 5 * 2)

        rUpdateKarg.update(id=10, width=7, height=8)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)

        rUpdateKarg.update(id=10, width=7, height=8, x=9)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        self.assertEqual(rUpdateKarg.x, 9)

        rUpdateKarg.update(y=14, height=10, id=6, x=19, width=3)
        self.assertEqual(rUpdateKarg.id, 6)
        self.assertEqual(rUpdateKarg.area(), 30)
        self.assertEqual(rUpdateKarg.x, 19)
        self.assertEqual(rUpdateKarg.y, 14)

    def test_to_dict(self):
        """ check if to_dictionary returns the dict as exected """
        r0 = Rectangle(4, 6, 8, 3, 12)
        expect_out = {'id': 12, 'width': 4, 'height': 6, 'x': 8, 'y': 3}
        self.assertEqual(r0.to_dictionary(), expect_out)


if __name__ == "__main__":
    unittest.main()
