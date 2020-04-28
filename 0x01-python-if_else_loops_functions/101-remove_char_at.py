#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    if (n < 0 or n > len(str)):
        return (str)
    else:
        for i in range(0, len(str)):
            if (i != n):
                ch = ch + str[i]
    return (ch)
