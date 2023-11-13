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
import pycodestyle


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

	def test_pep8_Amen(self):
		"""Tests pep8"""
		style = pycodestyle.StyleGuide(quiet=True)
		pycode = style.check_files(['models/amenity.py'])
		self.assertEqual(pycode.total_errors, 0, "fix your pycodestyle")

	def test_docstring_Amen(self):
		"""test for docstrings"""
		self.assertIsNotNone(self.amenity1.__doc__)

	def test_attribute(self):
		"""chekcing if amenity have attibutes"""
		self.assertTrue('id' in self.amenity1.__dict__)
		self.assertTrue('created_at' in self.amenity1.__dict__)
		self.assertTrue('updated_at' in self.amenity1.__dict__)
		self.assertTrue('name' in self.amenity1.__dict__)

	def test_inheritance(self):
		"""test if inheritance works"""
		self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

	def test_attrtype(self):
		"""test attr types in instance"""
		self.assertEqual(type(self.amenity1.name), str)


if __name__ == "__main__":
    unittest.main()
