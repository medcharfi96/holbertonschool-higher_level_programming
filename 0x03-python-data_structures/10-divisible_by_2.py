#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tab = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 != 0:
            tab.append(False)
        else:
            tab.append(True)
    return (tab)
