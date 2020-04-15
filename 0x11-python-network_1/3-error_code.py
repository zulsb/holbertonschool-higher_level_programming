#!/usr/bin/python3
"""
    Script that get http error code.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
