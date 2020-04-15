#!/usr/bin/python3
"""
    Script that takes a url and email, and sends
    a post request to the input url.
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    values = {"email": argv[2]}

    data = urllib.parse.urlencode(values).encode("utf-8")
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
