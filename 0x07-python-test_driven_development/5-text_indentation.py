#!/usr/bin/python3
"""
text indent° function
"""


def text_indentation(text):
    """
    Print text with two lines
    """
    new_string = ""
    zab =["?",":","."]
    bool1 = False
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range (0,len(text)):
        a = text[i - 1]
        if a in zab:
            bool1 = True
        bool2 = text[i] == " "
        if bool1 and bool2:
            text[i+1].replace(text[i],"")
        elif text[i] in zab:
            print(text[i])
        else:
            print(text[i], end="")

