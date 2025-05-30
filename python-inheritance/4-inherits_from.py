#!/usr/bin/python3
"""
This module is a module
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    from the specified class, otherwise return false
    """

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
