#!/usr/bin/python3
"""
Module 6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"
    """

    with open(filename, 'r') as openfile:
        return json.load(openfile)
