#!/usr/bin/python3
"""Unittest created for max_integer([...])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """
    Unit Testing class for max_integer
    unittest imported
    """

    def test_module_docstring(self):
        """Check: module docsting"""
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_function_docstring(self):
        """Check: function docstring"""
        function_doc = max_integer.__doc__
        self.assertTrue(len(function_doc) > 1)

    def test_list_of_numbers(self):
        """Check: test case with a numbers list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_of_zero(self):
        """Check: test case with a full zero list"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_character_in_list(self):
        """Check: test case with a tuple an a character on it"""
        with self.assertRaises(TypeError):
            max_integer((1, 2, 3, 'a'))

    def test_negative_number_list(self):
        """Check: test case with a single negative number"""
        self.assertEqual(max_integer([-1]), -1)

    def test_math_operations_list(self):
        """Check: test case with a list of operations"""
        self.assertEqual(max_integer([5 + 5, 3 * 2, 6 ** 3]), 216)

    def test_booleans(self):
        """Check: test case with a booleans list"""
        self.assertEqual(max_integer([True, False]), True)

    def test_tuple(self):
        """Check: test case with a tuple"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_inf_in_list(self):
        """Check: test case with a tuple with a inf on it"""
        self.assertEqual(max_integer((1, 2, 3, float('inf'))), float('inf'))

    def test_none_in_list(self):
        """Check: test case with a tuple  with a inf on it"""
        with self.assertRaises(TypeError):
            max_integer((1, 2, 3, None))

    def test_empty_tuple(self):
        """Check: test case with an empty tuple"""
        self.assertIsNone(max_integer(()))

    def test_empty_list(self):
        """Check: test case with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_none(self):
        """Check: test case with a None arg"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        """Check: test case with a string arg"""
        self.assertEqual(max_integer("hola"), 'o')

    def test_matrix(self):
        """Check: test case with a Matrix"""
        self.assertEqual(max_integer([[1, 2], [2, 1], [3, 4]]), [3, 4])

    def test_huge_number(self):
        """Check: test case with a huge number"""
        self.assertEqual(max_integer([126, 1e1010]), 1e1010)

    def test_tiny_number(self):
        """Check: test case with a tiny number"""
        self.assertEqual(max_integer([-126, 1e-1010]), 0.0)

    def test_hexadecimal_list(self):
        """Check: test case with hexadecimal numbers list"""
        self.assertEqual(max_integer([0x09, 0x51, 0x08]), 0x51)

if __name__ == "__main__":
    unittest.main()
