#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    else:
        m = 0
        for i in a_dictionary:
            if m <= a_dictionary[i]:
                m = a_dictionary[i]
    return(i)
