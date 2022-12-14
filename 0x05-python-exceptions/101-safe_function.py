#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException as a:
        print("Exception: {}".format(a), file=sys.stderr)
        return None
