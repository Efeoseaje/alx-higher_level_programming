#!/usr/bin/python3

"""a function that writes a string to a text file (UTF8) and returns
 the number of characters written
 """


def write_file(filename="", text=""):
    """
        a function that writes a string to a text file (UTF8) and returns
        the number of characters written

        Args:
            filename: The name of the file we want to write to

            text: The string we want to write to a text file

        Returns: the number of characters written
    """
    with open(filename, "w") as f:
        """ Write to the text file and return the number of characters"""
        nb_characters = f.write(text)
    return nb_characters
