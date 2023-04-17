#!/usr/bin/python3
""" This module contains the base class for other classes"""


class Base:
    """ Represents the base class for other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes a new base

        Args:
            id(int): The identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objectss
