#!/usr/bin/python3
"""
advanced class
"""


class MyInt(int):
    """ declaration class class """
    def __init__(self, val):
        self.__val = val

    def __eq__(self, nombre):
        """ inverse fnt ====>"""
        return self.__val != nombre

    def __ne__(self, nombre):
        """ inverse fnt != != != """
        return not self.__eq__(nombre)