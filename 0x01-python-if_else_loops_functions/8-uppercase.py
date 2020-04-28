#!/usr/bin/python3
def uppercase(str):
    ch = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            ch = ch + chr(ord(str[i]) - 32)
        else:
            ch = ch + str[i]
    print("{:s}".format(ch))
