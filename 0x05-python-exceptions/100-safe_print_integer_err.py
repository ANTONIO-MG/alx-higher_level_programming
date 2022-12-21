#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except BaseException as a:
        print("Exception: {}".format(a), file=sys.stderr)
        return False
    return True
