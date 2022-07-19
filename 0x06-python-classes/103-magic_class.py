#!/usr/bin/python3
"""MagicClas"""


class MagicClass:
    """Magic class that does the same as given bytecode (Circle)"""
    def __init__(self, radius=0):
        """Initialize radius

        Args:
            radius: radius of a circle

        Raises:
            TypeError: if radius is not int or float
        """
        sel.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """Returns the calculated area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """Returns the calculated circumference of a circle"""
        return 2 * math.pi * self.__radius
