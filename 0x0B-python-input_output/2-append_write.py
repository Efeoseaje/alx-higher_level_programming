#!/usr/bin/python3

"""a function that appends a string to a text file (UTF8) and returns
 the number of characters written
 """


def append_write(filename="", text=""):
    """
        a function that appends a string to a text file (UTF8) and returns
        the number of characters written

        Args:
            filename: The name of the file we want to append to

            text: The string we want to append to a text file

        Returns: the number of characters added
    """
    with open(filename, "a") as f:
        """ Append to the text file and return the number of characters"""
        nb_characters_added = f.write(text)
    return nb_characters_added
