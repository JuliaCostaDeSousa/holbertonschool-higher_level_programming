#!/usr/bin/python3
"""
module 4-square.py

This module defines a Square class to define a square by its size.
"""


class Square:
    """
    Class that defines a square by its size (private attribute)

    """

    def __init__(self, size=0):
        """
        Initialize a new square by its size

        Args:
            size (int) : size of the square
        """

        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the current square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the current square
        """

        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the area of the current square
        """

        return self.__size**2
