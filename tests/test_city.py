#!/usr/bin/python3
'''Unit tests for the City Class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict

'''
import unittest
from models.city import City
import os
import models
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unit tests for the instantation of City class'''

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_instance(self):
        self.assertIn(City(), models.storage.all().values())

    def test_TypeOf_id(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_stateid(self):
        _city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(_city))
        self.assertNotIn("state_id", _city.__dict__)

    def test_name(self):
        _city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(_city))
        self.assertNotIn("name", _city.__dict__)

    def test_uniqueIds(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_different_created_at(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_different_updated_at(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_args(self):
        _city = City(None)
        self.assertNotIn(None, _city.__dict__.values())

    def test_nokwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        _date = datetime.today()
        _dateFormat = _date.isoformat()
        _city = City(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(_city.id, "10111")
        self.assertEqual(_city.created_at, _date)
        self.assertEqual(_city.updated_at, _date)


class Test_Save(unittest.TestCase):
    '''Unit tests for save function in the City class'''

    @classmethod
    def setUp(self):
        try:
            os.rename("filename.json", "tempo")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tempo", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        _city = City()
        sleep(0.1)
        f_updated_at = _city.updated_at
        _city.save()
        self.assertLess(f_updated_at, _city.updated_at)

    def test_double_save(self):
        _city = City()
        sleep(0.1)
        f_updated_at = _city.updated_at
        _city.save()
        s_updated_at = _city.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        _city.save()
        self.assertLess(s_updated_at, _city.updated_at)

    def test_args_save(self):
        _city = City()
        with self.assertRaises(TypeError):
            _city.save(None)

    def test_save_updatedFiles(self):
        _city = City()
        _city.save()
        _cityid = "City." + _city.id
        with open("file.json", "r") as fl:
            self.assertIn(_cityid, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unit tests for to_dict function in City class'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(City().to_dict))

    def test_Keys_to_dict(self):
        _city = City()
        self.assertIn("id", _city.to_dict())
        self.assertIn("created_at", _city.to_dict())
        self.assertIn("updated_at", _city.to_dict())
        self.assertIn("__class__", _city.to_dict())

    def test_extraAttributes_to_dict(self):
        _city = City()
        _cityDict = _city.to_dict()
        self.assertEqual(str, type(_cityDict["id"]))
        self.assertEqual(str, type(_cityDict["created_at"]))
        self.assertEqual(str, type(_cityDict["updated_at"]))

    def test_contrast_to_dict(self):
        _city = City()
        self.assertNotEqual(_city.to_dict(), _city.__dict__)

    def test_args_to_dict(self):
        _city = City()
        with self.assertRaises(TypeError):
            _city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
