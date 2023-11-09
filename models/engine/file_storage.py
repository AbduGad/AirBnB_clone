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
	
	@property
	def all(self):
		return self.__objects
	
	@object.setter
	def new(self, obj):
		if obj:
			key = "{}.{}".format(obj.__class__.__name__, obj.id)
			self.__objects[key] = obj

	def save(self):
		for key, value in self.__objects.items():
			self.__objects[key] = value.to_dict()
		with open(self.__file_path, 'w') as f:
			json.dump(self.__objects, f)

	def reload(self):
		try:
			with open(self.__file_path, 'r') as f:
				data = json.load(f)
		except FileNotFoundError:
			pass
			


