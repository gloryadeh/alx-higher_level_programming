#!/usr/bin/python3
"""
This module defines the function add_integer()
Raises:
    TypeError: if a or b is not a number (integer or float)
"""


def add_integer(a, b=98):
    """
    print(__import__("my_module").my_function.__doc__)
    Adds two integers and returns the result of the addition
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
