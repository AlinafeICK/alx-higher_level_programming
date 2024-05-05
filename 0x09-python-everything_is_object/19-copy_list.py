#!/usr/bin/python3
"""A function that
    copies a list
    and returns a new list
    with a copy of the original list
    without modifying the original list.
"""


def copy_list(my_list):
    """
    Copy a list to a new list.

    Parameters:
    my_list (list): The list to be copied.

    Returns:
    list: A new list containing the elements of the input list.
    """
    new_list = []
    for i in my_list:
        new_list.append(i)
    return new_list
