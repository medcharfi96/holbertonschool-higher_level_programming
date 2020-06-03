#!/usr/bin/python3
"""
fonction de lecture
"""


def read_file(filename=""):
    """ lire un ficher    """
    with open(filename, encoding='UTF8') as fichier:
        for ligne in fichier:
            print(ligne, end="")
