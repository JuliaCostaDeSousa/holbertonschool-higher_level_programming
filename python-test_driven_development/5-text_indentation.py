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

    i = 0
    while text[i] == " ":
        i += 1

    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in ['.', '?', ':', '\n']:
            print("{}".format("\n"))
            while text[i + 1] == " ":
                i += 1
        i += 1
