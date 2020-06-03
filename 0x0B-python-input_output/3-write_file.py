#!/usr/bin/python3
"""
ecrire dans un fichier
"""


def write_file(filename="", text=""):
    """ fonction d'ecriture """
    with open(filename, mode="w", encoding="utf-8") as fichier:
        return(fichier.write(text))
