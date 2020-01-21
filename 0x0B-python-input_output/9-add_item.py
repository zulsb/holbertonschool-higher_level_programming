#!/usr/bin/python3
"""
    Module contains the load_from_json_file function.
"""


import sys
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file


arg = sys.argv[1:]
try:
    a = load("add_item.json")
except IOError:
    a = []
save(a + arg, "add_item.json")
