#!/usr/bin/python3
"""
enregistrer un json en fichier
"""

import json


def save_to_json_file(my_obj, filename):
    """ enregisterer json en fichier """
    with open(filename, mode='w', encoding='UTF8') as fichier:
        chaine = json.dumps(my_obj)
        fichier.write(chaine)
