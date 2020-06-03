#!/usr/bin/python3
"""
changer du json a un fichier
"""

import json


def load_from_json_file(filename):
    """enregister dun objet au json"""

    with open(filename, mode='r', encoding='UTF8') as fichier:
        return json.loads(fichier)
