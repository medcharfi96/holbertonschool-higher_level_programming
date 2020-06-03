#!/usr/bin/python3
"""
declaration de classe
"""


class Student:
    """ la classe etudiant """
    def __init__(self, first_name, last_name, age):
        """ initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """rendre un fichier json"""
        if type(attrs) is list:
            khra = {}
            for count in range(0, len(attrs)):
                if attrs[count] == self.__dict__:
                    khra[count] = self.__dict__[i]
            return khra
        return (self.__dict__)
