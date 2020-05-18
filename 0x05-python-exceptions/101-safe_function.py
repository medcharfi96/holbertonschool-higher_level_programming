#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as errer:
        print("Exception: {}".format(errer), file=sys.stderr)
