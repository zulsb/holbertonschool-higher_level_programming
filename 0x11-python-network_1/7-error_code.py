#!/usr/bin/python3
"""
    Script that get http error code.
"""
import requests
from sys import argv


if __name__ == "__main__":
    re = requests.get(argv[1])
    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))
    else:
        print(re.text)
