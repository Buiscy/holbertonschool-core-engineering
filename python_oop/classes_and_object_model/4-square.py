#!/usr/bin/env python3
"""This is a practice class"""


class Square:
    """This is a class of square"""

    def __init__(self, value=0):
        self.size = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

