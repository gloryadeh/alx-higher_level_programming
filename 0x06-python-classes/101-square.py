#!/usr/bin/python3
"""Square class with private instance attribute size"""


class Square:
    """Arguments:
            size: size of Square
            position: starting point of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        """Returns string version of a square"""
        if self.size == 0:
            return ""
        sq = "\n" * self.position[1]
        for i in range(self.size):
            sq += "{}{}".format(" " * self.position[0], "#" * self.size)
            if i < self.size - 1:
                sq += "\n"
        return sq

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
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """position: position of the sqaure

        setter validates that position is a tuple of 2 positive integers

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not self.__check_position(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __check_position(self, position):
        """ checks if position is a tuple of 2 positive integers

        Returns: True if position is valid, False otherwise
        """
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def area(self):
        """Returns the calculated area of a Square instance"""
        return self.size ** 2

    def my_print(self):
        """Prints to stdout the square with the character # or an empty
        line if size is 0, position indicates by spaces and new lines
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
