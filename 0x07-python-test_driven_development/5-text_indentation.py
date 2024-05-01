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

    if text == "":
        raise ValueError("text cannot be empty")

    prev_char = ""
    for char in text:
        if prev_char in [".", "?", ":"]:
            if char == " ":
                continue
            print("\n")
        print(char, end="")
        prev_char = char

    print("")
