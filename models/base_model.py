#!/usr/bin/python3
""" SuperClass module.
    Define common attributes and methods for AirBnB console
    Classes:
        BaseModel: set common attributes & methods
"""
from uuid import uuid4
import datetime
import models


class BaseModel():
    """
    defines all common attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        # print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """_summary_"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """_summary_"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
