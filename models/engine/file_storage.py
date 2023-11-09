#!/usr/bin/python3
"""
class that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json


class FileStorage():
    """
    Class for saving and loading data from files.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def classes(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.review import Review
        from models.city import City
        from models.place import Place
        from models.user import User
        from models.state import State

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
