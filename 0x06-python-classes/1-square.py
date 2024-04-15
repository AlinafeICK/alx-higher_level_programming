#!/usr/bin/python3
""" A module of class Square based on 0-square.py."""


class Square:
    """ A Square Class that defines a square with a private instance attribute: size"""

    def __init__(self, size):
        """ Initializes a new Square.
        
        Args:
            size (int): Size of new square.
            
        """
        self.__size = size

