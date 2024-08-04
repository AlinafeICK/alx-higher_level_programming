#!/usr/bin/python3
"""A class Student that defines a student by various attributes and methods."""


class Student:
    """Defines a student with first name, last name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to include in the
            returned dictionary. Defaults to None.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            raise TypeError("attrs must be a list of strings")

        if not all(isinstance(attr, str) for attr in attrs):
            raise TypeError("attrs must be a list of strings")

        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        from a JSON dictionary.

        Args:
            json (dict): Dictionary containing the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
