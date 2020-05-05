#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l != 0:
        nouveau = (l, sentence[0])
    else:
        nouveau = (l, None)
    return nouveau
