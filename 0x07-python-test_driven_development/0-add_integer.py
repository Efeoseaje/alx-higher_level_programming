#!/usr/bin/python3
""" A function that adds two integers"""


def add_integer(a, b=98):
    """ Function returns an integer
    Args:
        a (int or float): First argument
        b (int or float): Second argument
    Returns:
        Sum of the two arguments
    Raises:
        TypeError: if a or b is not an int or float
        """
    if type(a) is not int or float:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
