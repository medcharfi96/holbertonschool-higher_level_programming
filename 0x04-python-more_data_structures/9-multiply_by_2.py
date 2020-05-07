#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    jdid = a_dictionary.copy()
    for key in a_dictionary.keys():
        jdid[key] = a_dictionary[key] * 2
    return (jdid)
