#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    correct_names = []
    for name in names:
        if not name.startswith("__"):
            correct_names.append(name)
    correct_names.sort()
    for name in correct_names:
        print(name)

