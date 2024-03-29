#!/usr/bin/python3

"""function that writes an Object to a text file,using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """
        Writes an object to a text file using JSON representation.

        Args;
            Obj: The object to write to the file
            filename: The file to write to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
