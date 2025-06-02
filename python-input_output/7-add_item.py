#!/usr/bin/python3
"""
Module 6-load_from_json_file
"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    filename = "add_item.json"
    args_list = load_from_json_file(filename)
except FileNotFoundError:
    args_list = []

args_list.extend(argv[1:])
save_to_json_file(args_list, filename)
