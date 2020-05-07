#!/usr/bin/python3
def weight_average(my_list=[]):
    denom = 0
    devision = 0
    if len(my_list) != 0:
        for x in my_list:
            denom = denom + (x[0] * x[1])
            devision = devision + x[1]
    else:
        return 0
    return denom / devision
