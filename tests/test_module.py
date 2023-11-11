#!/usr/bin/python3
from models.base_model import BaseModel

class test_module():
	def __init__(self):
		self.name = "test"
		self.version = 1
		self.author = "Joe Bloggs"
		self.description = "This is a test module."
	
	def name(self):
		print(f"{self.name}")
