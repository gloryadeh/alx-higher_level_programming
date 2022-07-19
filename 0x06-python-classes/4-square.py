#!/usr/bin/python3
"""Square class with private instance attribute size"""


class Square:
    """Arguments:
            size: size of Square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """size: size of sqaure

        setter validates size is an integer and >= 0

        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the calculated area of a Square instance"""
        return self.size ** 2
