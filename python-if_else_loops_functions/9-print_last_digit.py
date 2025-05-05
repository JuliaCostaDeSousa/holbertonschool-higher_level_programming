#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    if number >= 10:
        print(number % 10, end="")
        return number % 10

    else:
        print(number, end="")
        return number
