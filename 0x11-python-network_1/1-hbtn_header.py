#!/usr/bin/python3
"""Python script that fetches a given argmument url using urllib

Uses urllib and sys packages
The value of this variable is different for each request

Usage:
    import urllib
    ./1-hbtn_header.py https://alx-intranet.hbtn.io
"""

from urllib.request import urlopen
import sys

with urlopen(sys.argv[1]) as item:
    """Opens the provided argument url"""
    response = item.headers

    for header, value in response.items():
        """ loops through the header values"""
        if header == "X-Request-Id":
            R_ID = f"{value}"

if __name__ == "__main__":
    """ this prevents the code from beeing executed when imported"""
    print(R_ID)
