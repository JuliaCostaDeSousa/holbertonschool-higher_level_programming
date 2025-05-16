#!/usr/bin/python3
"""
This module provides a function that prints My name is <first name> <last name>.

It handles strings.
If <first_name> and <last_name> strings, it raises a TypeError.

You are not allowed to import any module.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White

    """

    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
