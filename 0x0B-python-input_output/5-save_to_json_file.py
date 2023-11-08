#!/usr/bin/python3
"""This module contains the funtion save_to_json_file"""


import json
"""This module contains the Javasript Object Notation"""


def save_to_json_file(my_obj, filename):
    """This function saves a json representation into a file"""
    string = json.dumps(my_obj)
    with open(filename, mode='w', encoding="utf-8") as file:
        file.write(string)
