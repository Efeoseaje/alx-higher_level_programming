#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Private instance Size is instantiatized and raises exceptions"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """To retreive the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the right value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Define a public instance Area and return the current square value"""
    def area(self):
        return self.__size ** 2

    """Define a public instance methos that prints the square with #"""
    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
