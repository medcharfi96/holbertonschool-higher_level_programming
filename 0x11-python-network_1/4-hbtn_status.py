#!/usr/bin/python3
"""
fetch me fetch me feeeeeeeeeeet
"""


import requests
if __name__ == "__main__":
    requette = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(requette.text)))
    print("\t- content: {}".format(requette.text))
