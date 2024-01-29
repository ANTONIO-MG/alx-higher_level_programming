#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status using urllib

It uses the urllib package
The body of the response must be displayed like the following example
(tabulation before -)

Usage:
    import urllib
    ./0-hbtn_status.py
"""

from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as item:
    """Opens the provided argument url"""
    response = item.read()

if __name__ == "__main__":
    """ this prevents the code from beeing executed when imported"""
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
    print(f"\t- utf8 content: {response.decode('utf-8')}")
