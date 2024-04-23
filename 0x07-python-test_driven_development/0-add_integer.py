#!/usr/bin/python3
"""This is a module that adds two integers"""


def add_integer(a, b=98):
    """Our function takes in two arguments and returns a sum

    Args:
        a (int/float): integer argument
        b (int/float, optional): Second integer argument. Defaults to 98.

    Raise: TypeError
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
