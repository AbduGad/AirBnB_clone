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
	__file_path = 'Storage.json'
	__objects = {}
	
	@property
	def all(self):
		return self.__objects
	
	@object.setter
	def new(self, obj):
		if obj:
			key = "{}.{}".format(obj.__class__.__name__, obj.id)
			self.__objects[key] = obj

	def save(self):
