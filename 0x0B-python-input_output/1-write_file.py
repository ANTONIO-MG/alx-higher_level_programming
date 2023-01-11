#!/usr/bin/python3
"""
a function that writes a string to a file

ARGS:
filename - the name of the file to be created or updated
text -  the string to be written to the file
file_writter - theobject created
"""


def write_file(filename="", text=""):
	with open(filename, mode="w", encoding="utf-8") as file_writter:
		print(len(text))
