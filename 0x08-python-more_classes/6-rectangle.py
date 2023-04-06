#!/usr/bin/python3

"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Class that represents a retangle"""

    number_of_instances = 0
    """Class attribute that counts number of instances"""

    def __init__(self, width=0, height=0):
        """Definition and instantiation of a Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @height.setter
    def height(self, value):
        """To set the correct value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Definition of Area that returns rectangle area"""
        return int(self.__width) * (self.__height)

    def perimeter(self):
        """Definition of Perimeter that returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return int(2 * ((self.__width) + (self.__height)))

    def __str__(self):
        """Prints a rectangle with character '#' """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"  # Append a hash tag
            if i < self.__height - 1:
                rectangle += "\n"  # Append a new line
        return rectangle

    def __repr__(self):
        """return a string representation of a rectangle"""
        i = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return i

    def __del__(self):
        """Delete an instance of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
