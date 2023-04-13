#!/usr/bin/python3

""" A module that define a class Student"""


class Student:
    """ A class that defines a student by first name, last nema and age"""

    def __init__(self, first_name, last_name, age):
        """ Instantiation of a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student"""
        return self.__dict__
