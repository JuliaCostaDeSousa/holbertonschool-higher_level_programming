#!/usr/bin/python3
"""
This module provides a function that returns
if an object is EXACTLY from a specific class or not
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is from the specified class,
    otherwise return false 
    """

    return type(obj) is a_class
