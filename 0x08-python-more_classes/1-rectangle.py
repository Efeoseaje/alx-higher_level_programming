#!/usr/bin/python3

"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Class that represents a retangle"""
    def __init__(self, width=0, height=0):
        """Definition and instantiation of a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """To retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set the correct value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve the height"""
        return self.__height

    @width.setter
    def height(self, value):
        """To set the correct value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
