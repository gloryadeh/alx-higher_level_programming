#!/usr/bin/python3
"""
    This module prints a square with the character #

    Raises:
        TypeError: if type of size is not int
        ValueError: if size is less than 0
"""


def print_square(size):
    """
        Print a square with the # character
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
