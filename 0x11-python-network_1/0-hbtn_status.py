#!/usr/bin/python3
"""
donneer le lien
"""


import urllib.request
if __name__ == "__main__":
    lien = 'https://intranet.hbtn.io/status'
    requette = urllib.request.Request(lien)
    with urllib.request.urlopen(requette) as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
