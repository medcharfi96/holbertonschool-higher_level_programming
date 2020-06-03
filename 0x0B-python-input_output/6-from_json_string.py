#!/usr/bin/python3
"""
changer en mode json to string
"""


import json


def from_json_string(my_str):
    """fonction de json  en str """
    return json.loads(my_str)
