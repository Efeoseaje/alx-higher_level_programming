#!/usr/bin/python3

"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Definition and instantiation of a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """To retrieve the width"""
    @property
    def width(self):
        return self.__width

    """To set the correct value of width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """To retrieve the height"""
    @property
    def height(self):
        return self.__height

    """To set the correct value of height"""
    @width.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
