#!/usr/bin/python3

"""a function that returns an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """
        Converts a JSON string into a python object.

        Args;
            str: The JSON string to be converted.

        Returns: The python object"""
    from_json_string = json.loads(my_str)
    return from_json_string
