#!/usr/bin/python3
"""
module 8-rectangle.py

This module provides a Rectangle class
"""


class Rectangle:
    """
    Class that defines a rectangle.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle by its width and height

        Args:
            width (int) : width of the rectangle
            height (int) : height of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints in stdout the rectangle with the character #
        If width or height are equal to 0, prints an empty line
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        symbol = getattr(self, "print_symbol", Rectangle.print_symbol)

        for i in range(self.__height):
            for j in range(self.__width):
                result += str(symbol)
            if i != self.__height - 1:
                result += "\n"

        return result

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """

        width = self.__width
        height = self.__height

        return "Rectangle({}, {})".format(width, height)

    def __del__(self):
        """
        Deletes an instance of Rectangle
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
