#!/usr/bin/python3
"""
ecrire dans un fichier
"""


def append_write(filename="", text=""):
    """ fonction d'ecriture """
    with open(filename, mode="a", encoding="utf-8") as fichier:
        return(fichier.write(text))
