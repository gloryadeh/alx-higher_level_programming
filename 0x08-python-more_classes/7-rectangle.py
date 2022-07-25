#!/usr/bin/python3
"""Class Rectangle with private instance attribute width and height"""


class Rectangle:
    """an empty class called Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string of Rectangle instance using #, empty string"""
        if self.width == 0 or self.height == 0:
            return ""
        row = "{}".format(self.print_symbol) * self.width
        rect = row
        for i in range(self.height - 1):
            rect += "\n" + row
        return rect

    def __repr__(self):
        """Returns a string representation of
            the rectangle to be able to recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

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

    def area(self):
        """Returns the area of Rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of Rectangle"""
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.height + self.width)
        return perimeter
