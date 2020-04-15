#!/usr/bin/python3
"""
    Script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable.
"""
import requests
from sys import argv


if __name__ == "__main__":
    re = requests.get(argv[1])
    print(re.headers.get("X-Request-Id"))
