#!/usr/bin/python3
"""
Module 0-read_file
"""


def read_file(filename=""):
    """
    Reads a text file
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
