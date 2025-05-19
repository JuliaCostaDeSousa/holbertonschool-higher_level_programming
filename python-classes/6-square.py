#!/usr/bin/python3
"""
module 6-square.py

This module defines a Square class to define a square by its size.
"""


class Square:
    """
    Class that defines a square by its size (private attribute)

    """

    def __init__(self, size=0, position=(0, 0)):
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

        if not isinstance(position, (tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], (int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the current square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the current square
        """

        if not isinstance(value, (tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], (int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Returns the area of the current square
        """

        return self.__size**2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        If size is equal to 0, print an empty line
        """
        if self.size == 0:
            print()
            return
        
        for h in range(self.__position[1]):
            print()
        if self.__size != 0:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
