#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nv_l = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print('out of range')
            res = 0
        except TypeError:
            print('wrong type')
            res = 0
        except ZeroDivisionError:
            print('division by 0')
            res = 0
        finally:
            nv_l.append(res)
    return nv_l
