#!/usr/bin/python3

"""a function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """
        Creates an Object from a 'JSON file'.

        Args:
            filename: The JSON file from which object is created.

    """
    with open(filename) as f:
        return json.load(f)
