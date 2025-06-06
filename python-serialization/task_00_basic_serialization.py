#!/usr/bin/python3
"""
Module task_00_basic_serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize data and save it to JSON file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(data))

    pass


def load_and_deserialize(filename):
    """
    Load and deserialize
    """

    with open(filename, 'r') as openfile:
        return json.load(openfile)

    pass
