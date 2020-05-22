#!/usr/bin/python3
"""
Add integers
"""


def add_integer(a, b=98):
    """ Add function """
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    elif type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    return(int(a) + int(b))
