#!/usr/bin/python3
"""This module contains a function that prints a text with \
indentation"""


def text_indentation(text):
    """This function prints 'text' \
with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    if not text:
        raise TypeError('text must be a string')
    if text is None:
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == ':' or text[i] == '?':
            print(text[i])
            print()
            if i + 1 < len(text):
                if text[i + 1] == ' ':
                    i += 1
        else:
            print(text[i], end="")
        i += 1
