#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
        return ret
    except Exception as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return None
