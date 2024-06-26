#!/usr/bin/python3
""" A module of class Square based on 1-square.py."""


class Square:
    """A Square Class that defines a square
    with a private instance attribute: size
    """
    def __init__(self, size=0):
        """ Initializes a new Square.
        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
