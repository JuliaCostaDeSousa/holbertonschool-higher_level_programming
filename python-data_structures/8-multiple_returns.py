#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
