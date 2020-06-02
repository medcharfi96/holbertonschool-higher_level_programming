#!/usr/bin/python3
"""
function testing the type
"""


def is_same_class(obj, a_class):
    """function discription: test for the same type"""
    if type(obj) is not a_class:
        return False
    else:
        return True
