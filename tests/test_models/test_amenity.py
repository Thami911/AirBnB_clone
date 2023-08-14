#!/usr/bin/python3
"""Describes unittests for models/amenity.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Amenity class testing for instantiation Unittests."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amety = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amety.__dict__)

    def test_two_amenities_unique_ids(self):
        amety1 = Amenity()
        amety2 = Amenity()
        self.assertNotEqual(amety1.id, amety2.id)

    def test_two_amenities_different_created_at(self):
        amety1 = Amenity()
        sleep(0.05)
        amety2 = Amenity()
        self.assertLess(amety1.created_at, amety2.created_at)

    def test_two_amenities_different_updated_at(self):
        amety1 = Amenity()
        sleep(0.05)
        amety2 = Amenity()
        self.assertLess(amety1.updated_at, amety2.updated_at)

    def test_str_representation(self):
        day_t = datetime.today()
        day_repr = repr(day_t)
        amety = Amenity()
        amety.id = "123456"
        amety.created_at = amety.updated_at = day_t
        amety_str = amety.__str__()
        self.assertIn("[Amenity] (123456)", amety_str)
        self.assertIn("'id': '123456'", amety_str)
        self.assertIn("'created_at': " + day_repr, amety_str)
        self.assertIn("'updated_at': " + day_repr, amety_str)

    def test_args_unused(self):
        amety = Amenity(None)
        self.assertNotIn(None, amety.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        day_t = datetime.today()
        day_iso = day_t.isoformat()
        amety = Amenity(id="345", created_at=day_iso, updated_at=day_iso)
        self.assertEqual(amety.id, "345")
        self.assertEqual(amety.created_at, day_t)
        self.assertEqual(amety.updated_at, day_t)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Save method for Unittest with Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amety = Amenity()
        sleep(0.05)
        first_updated_at = amety.updated_at
        amety.save()
        self.assertLess(first_updated_at, amety.updated_at)

    def test_two_saves(self):
        amety = Amenity()
        sleep(0.05)
        first_updated_at = amety.updated_at
        amety.save()
        second_updated_at = amety.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amety.save()
        self.assertLess(second_updated_at, amety.updated_at)

    def test_save_with_arg(self):
        amety = Amenity()
        with self.assertRaises(TypeError):
            amety.save(None)

    def test_save_updates_file(self):
        amety = Amenity()
        amety.save()
        amty_mdl = "Amenity." + amety.id
        with open("file.json", "r") as x:
            self.assertIn(amty_mdl, x.read())


class TestAmenity_to_dict(unittest.TestCase):
    """to_dict method for Unittest for Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amety = Amenity()
        self.assertIn("id", amety.to_dict())
        self.assertIn("created_at", amety.to_dict())
        self.assertIn("updated_at", amety.to_dict())
        self.assertIn("__class__", amety.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amety = Amenity()
        amety.middle_name = "AirBnB"
        amety.my_number = 90
        self.assertEqual("AirBnB", amety.middle_name)
        self.assertIn("my_number", amety.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amety = Amenity()
        am_dict = amety.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        day_t = datetime.today()
        amety = Amenity()
        amety.id = "123456"
        amety.created_at = amety.updated_at = day_t
        tt_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': day_t.isoformat(),
            'updated_at': day_t.isoformat(),
        }
        self.assertDictEqual(amety.to_dict(), tt_dict)

    def test_contrast_to_dict_dunder_dict(self):
        amety = Amenity()
        self.assertNotEqual(amety.to_dict(), amety.__dict__)

    def test_to_dict_with_arg(self):
        amety = Amenity()
        with self.assertRaises(TypeError):
            amety.to_dict(None)


if __name__ == "__main__":
    unittest.main()
