#!/usr/bin/python3
"""
module 2-rectangle.py

This module provides a Rectangle class
"""


class Rectangle:
    """
    Class that defines a rectangle.

    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle by its width and height

        Args:
            width (int) : width of the rectangle
            height (int) : height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the current rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the current rectangle
        """

        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the current rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the current rectangle
        """

        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
