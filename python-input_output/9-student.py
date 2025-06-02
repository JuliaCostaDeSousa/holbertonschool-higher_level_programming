#!/usr/bin/python3
"""
Module 9-student
"""


class Student():
    """
    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary description for JSON serialization of an object
        """

        return self.__dict__
