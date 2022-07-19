#!/usr/bin/python3
"""Square with private instance attribute size"""


class Square:
    """Arguments:
            size: size of Square
    """
    def __init__(self, size=0):
        self.__size = size
