#!/usr/bin/python3
"""
description du head
"""


import urllib.request
from sys import argv
if __name__ == '__main__':
    requette = urllib.request.Request(argv[1])
    with urllib.request.urlopen(requette) as rps:
        page = rps.info().get("X-Request-Id")
        print(page)
