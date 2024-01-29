#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status using urllib

The email must be sent in the email variable
Uses the urllib and sys packages

Usage:
    import urllib
    ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
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
