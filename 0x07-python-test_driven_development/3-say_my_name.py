#!/usr/bin/python3
"""
This module prints a string

Raises:
    TypeError: if first_name and last_name are not strings
"""


def say_my_name(first_name, last_name=""):
    """Prints a string showing name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
