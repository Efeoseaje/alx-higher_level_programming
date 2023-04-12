#!/usr/bin/python3

""" A function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """
        filename: This is the name of the file we want to open

        Returns: the file object
    """
    with open(filename) as f:
        print(f.read(), end="")
