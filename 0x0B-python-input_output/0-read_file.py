#!/usr/bin/python3
"""
Function that prints out the content of a file

ARGS:
filename - the name with the extension of the file to be read.
reading - the variable holding the read method
"""


def read_file(filename=""):
	with open(filename, encoding="utf-8") as reading:
		print(reading.read())
