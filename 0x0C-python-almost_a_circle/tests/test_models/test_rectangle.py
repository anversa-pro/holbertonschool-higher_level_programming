#!/usr/bin/python3
""" Module for test the Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    "Testing suite for Rectangle class"
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

if __name__ == "__main__":
    unittest.main()