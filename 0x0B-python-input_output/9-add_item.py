#!/usr/bin/python3

from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
text = ""
try:
    with open(filename, mode='r', encoding='UTF-8') as fichier:
        json.load(fichier)
except FileNotFoundError:
    ret = []
ret = ret + argv[1:]
chaine = json.dumps(ret)
fichier.write(chaine)
