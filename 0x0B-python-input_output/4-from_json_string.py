#!/usr/bin/python3
"""This module contains the function fro_json_string"""


import json
"""This module contains the Javasript Object Notation"""


def from_json_string(my_str):
    """returns a json representation of a string"""
    return json.loads(my_str)
