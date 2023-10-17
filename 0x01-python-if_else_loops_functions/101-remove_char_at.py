#!/usr/bin/python3
def remove_char_at(strn, n):
    string = ""
    for i in range(len(strn)):
        if i == n:
            continue
        string += (strn[i])
    return string
