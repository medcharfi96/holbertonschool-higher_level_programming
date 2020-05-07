#!/usr/bin/python3
def roman_to_int(roman_string):
    val = 0
    if roman_string is None:
        return 0
    tr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    long = len(roman_string)
    for i in range(0, long):
        if roman_string[i] in tr:
                if i > 0 and tr[roman_string[i]] > tr[roman_string[i - 1]]:
                    val -= tr[roman_string[i]]
                else:
                    val += tr[roman_string[i]]
        else:
            return 0
    if val < 0:
        val = val * -1
    return val
