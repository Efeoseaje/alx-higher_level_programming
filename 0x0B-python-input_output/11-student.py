#!/usr/bin/python3

""" A module that define a class Student"""


class Student:
    """ A class that defines a student by first name, last name and age"""

    def __init__(self, first_name, last_name, age):
        """ Instantiation of a Student

            Args:
                first_name: First name of the student
                last_name: Last name of the student
                age: Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student

            Args:
            attrs: A list of strings specifying attribute names to retrieve.
                If None, all attributes will be retrieved. Default is None.

            Returns:
            dict: A dictionary representation of the Student instance.
        """
        if (type(attrs) == list and all(type(attr) == str for attr in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student"""
        for attr, value in json.items():
            setattr(self, attr, value)
