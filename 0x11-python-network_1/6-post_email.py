#!/usr/bin/python3
"""
    Script that takes a url and email, and sends
    a post request to the input url.
"""
import requests
from sys import argv


if __name__ == "__main__":
    values = {"email": argv[2]}

    re = requests.post(argv[1], data=values)
    print(re.text)
