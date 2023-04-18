#!/usr/bin/python3
""" This module contains a rectangle class """

from models.base import Base


class Rectangle(Base):
    """ This represents a rectangle that inheris from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a new Rectangle

        Args:
            width(int): Defines the with of the rectangle.
            height(int): Defines the height of the rectangle.
            x(int): Defines the x cordinate of the rectangle.
            y(int): Defines the y cordinate of the rectangle.
            id(int): Defines the identity of the rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieves the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width and ensures it gets the right value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height and ensures it gets the right value """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieves the x cordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x cordinate and ensures it gets the right value """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieves the y cordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the y cordinate and ensures it gets the right value """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle instance with '#' """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Overides the __str__ method """
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
