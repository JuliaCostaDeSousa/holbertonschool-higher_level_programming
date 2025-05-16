#!/usr/bin/python3
"""
This module gives a function that prints a square with the character #.

It handles an integer.
If size is not an integer, it raises a TypeError.

You are not allowed to import any module.
"""


def print_square(size):
    """
    Prints a square with the character #.

    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(1)
    #

    """

    if not isinstance(size, (int)) or (isinstance(size, (float)) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 1:
        print("#")
    elif size > 1:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
