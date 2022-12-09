"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    holder = items
    for word in holder:
        counteR = str(word)
        if counteR in frequencies.keys():
            frequencies[counteR] += 1
        else:
            frequencies[counteR] = 1
    return frequencies
