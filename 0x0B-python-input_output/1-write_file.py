#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """writes to a file or overwrites a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        nb = file.write(text)
        return nb
