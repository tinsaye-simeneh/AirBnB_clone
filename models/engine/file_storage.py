#!/usr/bin/python3

"""
This module contains the prototype for FileStorage class.
"""

from models.base_model import BaseModel
import json
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """Serialises __objects to the JSON file (path: __file_path)"""
        d = {k: v.to_dict()
             for k, v in self.__objects.items()}
        with open(self.__file_path, mode='w') as f:
            json.dump(d, f)

    def reload(self):
        """Deserialises the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                d = json.load(f)
                for k, v in d.items():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))

    def reset(self):
        """Reset all objects in __objects"""
        self.__objects = {}
