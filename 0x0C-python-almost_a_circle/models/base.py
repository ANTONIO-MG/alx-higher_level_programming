#!/usr/bin/python3
"""

This is the base of the model. it has some specific attributes such as
the id attribute of all classes that extend
from Base and avoid duplicate the same code int eh chikldren classes.

"""

from os import path
import json


class Base:

    """the Base class that every other class will inherit from
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        the initialisation of the base class
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """converst the data into a json string
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves the infomation onto a file
        """

        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """
        from json to a python opject/sring
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates a dictionary out of a class
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)
        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loads data from a file
        """

        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

        for elem in objs:
            instances.append(cls.create(**elem))

        return instances
