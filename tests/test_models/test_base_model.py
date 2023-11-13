#!/usr/bin/python3
"""Tests the basemodels"""
import sys
"""sys.path.append('/mnt/c/Users/pc/OneDrive/Desktop/\
                Alx/ALX Programing/AirBnB_clone')"""
import unittest
import os
from models.base_model import BaseModel
import pycodestyle
import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test base model class."""

    @classmethod
    def setUpClass(cls):
        cls.testBase = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.testBase
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_basemodel(self):
        """Check that code is PEP8 compliant."""
        style_pycode = pycodestyle.StyleGuide(quiet=True)
        pip = style_pycode.check_files(['models/base_model.py'])
        self.assertEqual(pip.total_errors, 0, "fix your code")

    def test_check_functions(self):
        """Check if all functions are defined correctly."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attribute_basemodel(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save(self):
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict(self):
        copy = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, 'BaseModel')
        self.assertIsInstance(copy['created_at'], str)
        self.assertIsInstance(copy['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
