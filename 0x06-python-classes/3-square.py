#!/usr/bin/python3
"""Square class with private instance attribute size"""


class Square:
    """Arguments:
            size: size of Square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the calculated area of a Square instance"""
        return self.__size ** 2
