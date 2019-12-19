#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        Keymax = max(a_dictionary, key=a_dictionary.get)
        return Keymax
    return None
