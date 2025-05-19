#!/usr/bin/python3
"""
module 1-square.py

This module defines a Square class to define a square by its size.
"""


class Square:
    """
    Class that defines a square by its size (private attribute)

    """

    def __init__(self, size = 0):
        """
        Initialize a new square by its size

        Args:
            size : size of the square
        """
        self.__size = size
