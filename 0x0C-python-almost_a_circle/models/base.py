#!/usr/bin/python3
"""defines base class"""
import json


class Base:
    """A base class for future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing id
        Args:
            id(int): number of instance class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """static method that returns json string
            representation of a list dictionary
        Args:
            list_dictionaries: list dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            ret = json.dumps(list_dictionaries)
            return ret

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes json string
            representation of a list object
        Args:
            list_objs: list object of a class"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
