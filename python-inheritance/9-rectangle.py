#!/usr/bin/python3
"""
This module provides the Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes an instance with a width and a height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        Returns the rectangle description
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Returns the rectangle area
        """

        return self.__width * self.__height
