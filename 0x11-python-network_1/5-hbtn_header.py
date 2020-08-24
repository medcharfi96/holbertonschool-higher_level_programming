#!/usr/bin/python3
"""
affichage des donner dans une variable
"""


import requests
from sys import argv
if __name__ == '__main__':
    rquette = requests.get(argv[1])
    print(rquette.headers.get('X-Request-Id'))
