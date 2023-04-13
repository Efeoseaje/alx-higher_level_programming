#!/usr/bin/python3

"""a function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
        Converts a Python object into its JSON representation as a string.

        Args;
            Obj: The Python object to be converted.

        Returns:
            str: The JSON representation of the object as string"""
    to_json_string = json.dumps(my_obj)
    return to_json_string
