#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = b1 = 0
    if len(tuple_a) != 0 and len(tuple_a) != 1:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    elif len(tuple_a) == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = a2 = 0

    if len(tuple_b) != 0 and len(tuple_b) != 1:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    elif len(tuple_b) == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = b2 = 0
    rtup = (a1 + b1, a2 + b2)
    return(rtup)
