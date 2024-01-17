#!/usr/bin/python3
""" Test module for Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test class for Amenity model """

    def __init__(self, *args, **kwargs):
        """ Initializes test_Amenity instance """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test the 'name' attribute """
        new = self.value()
        self.assertEqual(type(new.name), str)
