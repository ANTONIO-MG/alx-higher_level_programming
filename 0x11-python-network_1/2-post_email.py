#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status using urllib

Return: returns the class type, content and encoding method.
"""

import urllib.request
import urllib.parse
from sys import argv

string = {"email": argv[2]}
token = urllib.parse.urlencode(string)
token = token.encode('ascii')

with urllib.request.Request(argv[1], data=token, method='POST') as item:
    """Opens the provided argument URL"""
    response = urllib.request.urlopen(item)
    content = response.read().decode('utf-8')

if __name__ == "__main__":
    """ this prevents the code from beeing executed when imported"""
    print(content)
