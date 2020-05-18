#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if (i < a or i == a):
                res = res + (a ** b / i)
            else:
                raise Exception('Too far')
        except:
            res = b + a
            break
    return res
