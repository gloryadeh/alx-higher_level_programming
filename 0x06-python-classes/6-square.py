#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
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
        return self.__position

    @position.setter
    def position(self, value):
        if not self.__check_position(value):
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __check_position(self, position):
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
