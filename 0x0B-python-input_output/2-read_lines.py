#!/usr/bin/python3
"""
fonction de compter les lignes
"""


def read_lines(filename="", nb_lines=0):
    """ lire un ficher    """
    i = 0
    with open(filename, encoding='UTF8') as fichier:
        for ligne in fichier:
            i = i + 1
    with open(filename, encoding='UTF8') as fichier:
        if nb_lines <= 0 or nb_lines > i:
            for ligne in fichier:
                print(ligne, end="")
        else:
            for ligne in range(0, nb_lines):
                print(fichier.readline(), end="")
