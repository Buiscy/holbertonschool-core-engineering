#!/usr/bin/env python3
"""This is a practice class"""


class Square:
    """This is a class of square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__():
        return f"Beans"

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        i = 0
        j = 0
        value = self.__size
        if value == 0:
            print("")

        while i < value:
            while j < value:
                print("#", end="")
                j += 1
            print("")
            j = 0
            i += 1
