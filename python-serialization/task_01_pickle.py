#!/usr/bin/python3
"""
Module task_01_pickle
"""
import pickle


class CustomObject():
    """
    Class to serialize object with pickle
    """

    def __init__(self, name, age, is_student):
        """
        This method initializes a student
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        This method serializes a student
        """

        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        This method deserializes a file
        """

        with open(filename, 'rb') as f:
            return pickle.load(f)

    def display(self):
        """
        Display info
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
