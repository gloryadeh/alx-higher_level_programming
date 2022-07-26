#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none_value(self):
        """
            Testing when None is passed
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_right_output(self):
        """
            Testing when passing argument that should
            produce correct output
        """
        self.assertEqual(max_integer([3, -5, 9, 2]), 9)

    def test_empty_list(self):
        """
            Testing an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_no_parameter(self):
        """
            Testing no parameter
        """
        self.assertIsNone(max_integer())

    def test_equal_value(self):
        """
            Testing when all values in the list are
            equal
        """
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_no_int(self):
        """
            Testing with values in the list that are not int
        """
        with self.assertRaises(TypeError):
            max_integer([2, "good", 4, "u"])

    def test_only_neg(self):
        """
            Testing with negative numbers
        """
        self.assertEqual(max_integer([-3, -5, -9, -2]), -2)

    def test_beg(self):
        """
            Testing when first element of list is the
            only unique element
        """
        self.assertEqual(max_integer([20, 2, 2, 2, 2]), 20)

    def test_one(self):
        """
            Testing with just one element in list
        """
        self.assertEqual(max_integer([3]), 3)
