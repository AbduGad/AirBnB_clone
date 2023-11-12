#!/usr/bin/python3
"""
testing aminitey class
"""
"""import sys
sys.path.append('/mnt/c/Users/pc/OneDrive/Desktop/\
	Alx/ALX Programing/AirBnB_clone')"""

import unittest
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
import os


class test_amenity(unittest.TestCase):
	"""this is an amenity test"""

	@classmethod
	def setUpClass(cls):
		cls.amenity1 = Amenity()
	
	@classmethod
	def tearDownClass(cls):
		del cls.amenity1
		try:
			os.remove(storage.__file_path)
		except Exception:
			pass
