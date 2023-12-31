#!/usr/bin/python3
"""
class that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.place import Place
from models.user import User
from models.state import State


class FileStorage():
    """
    Class for saving and loading data from files.
    """
    __file_path = 'file.json'
    __objects = {}

    def classes(self):

        classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "Review": Review,
            "City": City,
            "Place": Place,
            "User": User,
            "State": State
        }
        return classes

    def all(self):
        """returns __objects attribute"""
        return self.__objects

    def new(self, obj):
        """new
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save
        """
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """reload
        """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                obj = eval(value['__class__'])(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
