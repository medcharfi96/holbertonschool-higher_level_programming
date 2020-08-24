#!/usr/bin/python3
"""
envoyer un email
"""


import urllib.request
from sys import argv
if __name__ == "__main__":
    lien = urllib.parse.urlencode({'email': argv[2]})
    lien = lien.encode('ascii')
    requette = urllib.request.Request(argv[1], lien)
    with urllib.request.urlopen(requette) as rps:
        the_page = rps.read()
        print(the_page.decode("utf-8"))
