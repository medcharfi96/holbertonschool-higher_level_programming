#!/usr/bin/python3
"""
debut la cllasse de base
"""


class Base:
    """
    description de la classe de base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method of class Base
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
