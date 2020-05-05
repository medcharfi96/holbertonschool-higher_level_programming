#!/usr/bin/python3
def no_c(my_string):
    nouveau = ""
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            nouveau = nouveau + my_string[i]
    return nouveau
