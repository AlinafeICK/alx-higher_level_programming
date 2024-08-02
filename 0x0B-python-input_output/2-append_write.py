#!/usr/bin/python3
"""A function that appends a string at the end of a file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a file
    and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
