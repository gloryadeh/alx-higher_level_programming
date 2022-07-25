#!/usr/bin/python3
"""Class Rectangle with private instance attribute width and height"""


class Rectangle:
    """an empty class called Rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """width: width of a rectangle

        setter checks if type is int and if value is < 0

        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height: height of a rectangle

        setter checks if type is int and if value is < 0

        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
