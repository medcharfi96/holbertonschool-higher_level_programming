#!/usr/bin/python3
"""
add attribute function
"""


def add_attribute(objt, nm, val):
    """ add fn """
    if hasattr(objt, "__dict__"):
        setattr(objt, nm, val)
    else:
        raise TypeError("can't add new attribute")