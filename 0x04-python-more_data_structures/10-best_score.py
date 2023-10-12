#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = 0
    for k, v in a_dictionary.items():
        if v > value:
            value = v
            best = k
    return best
