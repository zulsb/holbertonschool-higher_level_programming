#!/usr/bin/python3
"""
    Script that takes my Github credentials (username and password)
    and uses the Github API to display your id.
"""
import requests
from sys import argv


if __name__ == "__main__":
    re = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(re.json().get("id"))
