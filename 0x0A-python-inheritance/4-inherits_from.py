#!/usr/bin/python3
"""
function descr
"""


def inherits_from(obj, a_class):
    """ test inhrit"""
    if not isinstance(obj, a_class) or type(obj) is a_class:
        return False
    else:
        return True
