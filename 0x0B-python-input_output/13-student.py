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
        if type(attrs) is not list:
            return self.__dict__
        if type(attrs) is list:
            khra = {}
            for count in attrs:
                if count is not str and count in self.__dict__:
                    khra[count] = self.__dict__[count]
            return khra

    def reload_from_json(self, json):
        """ fonction de refléchir """
        for k, valeur in json.items():
            self.__dict__[k] = valeur
