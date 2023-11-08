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
	__file_path = 'None'
	__objects = {}
	