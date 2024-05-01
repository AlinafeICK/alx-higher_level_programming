#!/usr/bin/python3
"""
Text indentation module
Prints text with proper indentation
"""


def text_indentation(text):
    """Print text with proper indentation.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.
        ValueError: If `text` is an empty string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end='')
        if text[i] == '\n' or text[i] in ".?:":
            if text[i] in ".?:":
                print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
