#!/usr/bin/python3
""" unittest """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenity(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ create instance """
        cls.ins = Amenity()

    @classmethod
    def teardown(cls):
        """ Delete instance """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_doc(self):
        """ test model doc """
        self.assertNotEqual(len(Amenity.__doc__), 0)

    def test_attr(self):
        """ test model attributes """
        self.assertEqual(hasattr(self.ins, "name"), True)

    def test_type(self):
        """ test type of object """
        self.assertEqual(type(self.ins.name), str)

    def test_isinstance(self):
        """ test isinstance """
        self.assertTrue(isinstance(self.ins, Amenity))


if __name__ == '__main__':
    unittest.main()
