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

    def to_json(self):
        """rendre un fichier json"""
        return (self.__dict__)
