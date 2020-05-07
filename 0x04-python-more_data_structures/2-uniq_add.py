#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    newlist = []
    for i in my_list:
        if i not in newlist:
            newlist.append(i)
    for i in newlist:
        res = res + i
    return res
