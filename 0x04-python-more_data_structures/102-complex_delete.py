#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    liste_key_sup = []
    for key, val in a_dictionary.items():
        if val == value:
            liste_key_sup.append(key)
    for i in liste_key_sup:
        a_dictionary.pop(i, None)
    return a_dictionary
