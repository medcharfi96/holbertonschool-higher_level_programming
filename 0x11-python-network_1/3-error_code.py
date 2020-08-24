#!/usr/bin/python3
"""
give me the error
"""


import urllib.request
import urllib.error
from sys import argv
if __name__ == "__main__":
    requette = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(requette) as rps:
            page = rps.read()
            print(page.decode("ascii"))
    except urllib.error.HTTPError as erreure:
        print("Error code: {}".format(erreure.code))
