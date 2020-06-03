#!/usr/bin/python3
"""
fonction de compter les lignes
"""


def number_of_lines(filename=""):
    """ lire un ficher    """
    i = 0
    with open(filename, encoding='UTF8') as fichier:
        for ligne in fichier:
            i = i + 1
    return(i)
