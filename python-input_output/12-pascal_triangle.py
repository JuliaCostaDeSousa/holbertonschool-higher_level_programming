#!/usr/bin/python3
"""
Module 12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle:
    """

    if n <= 0:
        return []
    elif n == 1:
        return [[n]]
    else:
        