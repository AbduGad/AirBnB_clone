#!/usr/bin/python3
"""Tests city"""
import unittest
import pycodestyle
import os
from models.user import User
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """unittests for basemodel"""

    @classmethod
    def setUp(cls):
        """creates class"""
        cls.user1 = User()
        cls.user1.email = "email"
        cls.user1.password = "xxx"
        cls.user1.first_name = "first name"
        cls.user1.last_name = "last name"

    @classmethod
    def tearDown(cls):
        """deletes test class"""
        del cls.user1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """tests pycodestyle"""
        pycode = pycodestyle.StyleGuide(quiet=True)
        check = pycode.check_files(['models/user.py'])
        self.assertEqual(check.total_errors, 0, "fix pycodestyle")

    def test_init_and_class_variables(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.user1, User))
        self.assertTrue(issubclass(type(self.user1), BaseModel))
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))
        self.assertTrue('password' in self.user1.__dict__)
        self.assertTrue('first_name' in self.user1.__dict__)
        self.assertTrue('last_name' in self.user1.__dict__)

    def test_save(self):
        self.user1.save()
        self.assertTrue(self.user1.updated_at != self.user1.created_at)

    def test_strings(self):
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.first_name), str)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.user1), True)


if __name__ == '__main__':
    unittest.main()
