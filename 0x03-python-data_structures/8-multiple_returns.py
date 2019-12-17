#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_re = len(sentence)
    if sentence:
        return (tuple_re, sentence[0])
    else:
        return (tuple_re, None)
