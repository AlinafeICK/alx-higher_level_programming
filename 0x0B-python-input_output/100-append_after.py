#!/usr/bin/python3
"""A function that inserts a line of text to a file,
after each line containing a specific string:"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file,
    after each line containing a specific string:"""
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)
