#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status using urllib

Return: returns the class type, content and encoding method.
"""

import urllib


with urllib.request.urlopen(sys.argv[1]) as item:
    response = item.read()

if __name__ == "__main__":
    """ this prevents the code from beeing executed when imported"""
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
    print(f"\t- utf8 content: {response.decode('utf-8')}")
