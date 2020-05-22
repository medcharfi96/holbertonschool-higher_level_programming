#!/usr/bin/python3
"""
text indent° function
"""


def text_indentation(text):
    """ Print text with two lines """

    zab = ["?", ":", "."]
    test1 = False
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(0, len(text)):
        prev = text[i - 1]
        if prev in zab:
            test1 = True
        test2 = text[i] == " "
        if test1 and test2:
            print(text[i], end="")
        elif text[i] in zab:
            print(text[i])
            print()
        else:
            print(text[i], end="")
    print()
