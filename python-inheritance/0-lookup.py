#!/usr/bin/python3
"""
This module provides a function that returns 
the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods
    of an object
    """

    if not obj:
        return None
    
    return dir(obj)
