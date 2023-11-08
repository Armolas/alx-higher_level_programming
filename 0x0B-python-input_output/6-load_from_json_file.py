#!/usr/bin/python3
"""This module contains a function that creates object from
a JSON file"""


import json
"""This module contains the Javasript Object Notation"""


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, encoding="utf-8") as myFile:
        string = myFile.read()
    return json.loads(string)
