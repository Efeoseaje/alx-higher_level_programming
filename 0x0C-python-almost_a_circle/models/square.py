#!/usr/bin/python3
""" This module contains a Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This represents a square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square

        Args:
            Size(int): Defines the size of the Square.
            x(int): Defines the x cordinate of the Square.
            y(int): Defines the y cordinate of the Square.
            id(int): Defines the identity of the Square.

        Raises:
            TypeError: If either of size is not an int.
            ValueError: If either of size <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves the size of the square """
        return self.__width

    @size.setter
    def width(self, value):
        """ Sets the size and ensures it gets the right value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """ Overides the __str__ method """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
