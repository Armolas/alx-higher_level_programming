#!/usr/bin/python3
"""This module contains a function that appand to a file"""


def append_write(filename="", text=""):
    """appends text to an existing file or creates a new one"""
    with open(filename, mode='a', encoding='utf-8') as file:
        nb = file.write(text)
        return nb
