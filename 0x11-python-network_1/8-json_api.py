#!/usr/bin/python3
"""
    Script that takes in a letter and sends a POST request.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    values = {"q": letter}
    re = requests.post(url, data=values)

    try:
        dic = re.json()
        id = dic.get("id")
        name = dic.get("name")
        if dic:
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
