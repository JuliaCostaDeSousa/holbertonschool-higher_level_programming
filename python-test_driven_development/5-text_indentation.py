#!/usr/bin/python3
"""
This module gives a function that prints a text
with 2 new lines after each of these characters: ., ? and :

It handles a string.
If text is not a string, it raises a TypeError.

You are not allowed to import any module.
"""


def text_indentation(text):
    """
    Prints a text
    with 2 new lines after each of these characters: ., ? and :

    >>> text_indentation(".txt?")

    txt

    >>> text_indentation("txt")
    txt
    """

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    text_line = []
    for character in text:
        text_line.append(character)
        print(character, end="")
        if character in ['.', '?', ':']:
            while text_line[0] == " ":
                line = line[1:]
            while text_line[-1] == " ":
                line = line[:-1]
            print("\n")
            line = []
