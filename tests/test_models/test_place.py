#!/usr/bin/python3
'''Unit tests for Place Class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict

'''
import unittest
from models.place import Place
import os
import models
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unit tests for Place class instantiation '''

    def test_zero_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_TypeOf_id(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_cityid(self):
        _place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(_place))
        self.assertNotIn("city_id", _place.__dict__)

    def test_name(self):
        _place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(_place))
        self.assertNotIn("name", _place.__dict__)

    def test_description(self):
        _place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(_place))
        self.assertNotIn("desctiption", _place.__dict__)

    def test_numberOfRooms(self):
        _place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(_place))
        self.assertNotIn("number_rooms", _place.__dict__)

    def test_numberOfBathrooms(self):
        _place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(_place))
        self.assertNotIn("number_bathrooms", _place.__dict__)

    def test_maxGuests(self):
        _place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(_place))
        self.assertNotIn("max_guest", _place.__dict__)

    def test_price_by_night(self):
        _place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(_place))
        self.assertNotIn("price_by_night", _place.__dict__)

    def test_latitude(self):
        _place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(_place))
        self.assertNotIn("latitude", _place.__dict__)

    def test_longitude(self):
        _place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(_place))
        self.assertNotIn("longitude", _place.__dict__)

    def test_amenity_ids(self):
        _place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(_place))
        self.assertNotIn("amenity_ids", _place.__dict__)

    def test_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_created_at(self):
        place1 = Place()
        sleep(0.1)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_updated_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_unusedArgs(self):
        _place = Place(None)
        self.assertNotIn(None, _place.__dict__.values())

    def test_Zero_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        _date = datetime.today()
        _dateFormat = _date.isoformat()
        _place = Place(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(_place.id, "10111")
        self.assertEqual(_place.created_at, _date)
        self.assertEqual(_place.updated_at, _date)

class Test_Save(unittest.TestCase):
    '''Unit tests for save function in place class'''

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        _place = Place()
        sleep(0.1)
        first_updated_at = _place.updated_at
        _place.save()
        self.assertLess(first_updated_at, _place.updated_at)

    def test_double_save(self):
        _place = Place()
        sleep(0.1)
        f_updated_at = _place.updated_at
        _place.save()
        s_updated_at = _place.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        _place.save()
        self.assertLess(s_updated_at, _place.updated_at)

    def test_saveArg(self):
        _place = Place()
        with self.assertRaises(TypeError):
            _place.save(None)

    def test_updatesFile_save(self):
        _place = Place()
        _place.save()
        _placeid = "Place." + _place.id
        with open("file.json", "r") as fl:
            self.assertIn(_placeid, fl.read())


class TestPlace_to_dict(unittest.TestCase):
    '''Unittests for to_dict function in Place class'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_Keys_to_dict(self):
        _place = Place()
        self.assertIn("id", _place.to_dict())
        self.assertIn("created_at", _place.to_dict())
        self.assertIn("updated_at", _place.to_dict())
        self.assertIn("__class__", _place.to_dict())

    def test_extra_to_dict(self):
        _place = Place()
        _place.middle_name = "Africa"
        _place.my_number = 123
        self.assertEqual("Africa", _place.middle_name)
        self.assertIn("my_number", _place.to_dict())

    def test_datetime_to_dict(self):
        _place = Place()
        _place_dict = _place.to_dict()
        self.assertEqual(str, type(_place_dict["id"]))
        self.assertEqual(str, type(_place_dict["created_at"]))
        self.assertEqual(str, type(_place_dict["updated_at"]))

    def contract_to_dict(self):
        _place = Place()
        self.assertNotEqual(_place.to_dict(), _place.__dict__)

    def test_arg_to_dict(self):
        _place = Place()
        with self.assertRaises(TypeError):
            _place.to_dict(None)


if __name__ == "__main__":
    unittest.main()
