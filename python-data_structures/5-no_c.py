#!/usr/bin/python3
def no_c(my_string):
    new_string_list = []
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_string_list.append(letter)
    return ' '.join(new_string_list)
