#!/usr/bin/python3
'''Unit tests for User class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict
'''
import unittest
import models
from models.user import User
import os
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unittests for user class instances'''

    def test_zero_Instantiation(self):
        self.assertEqual(User, type(User()))

    def test_new_instance(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_updated_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_UnusedArgs(self):
        _user = User(None)
        self.assertNotIn(None, _user.__dict__.values())

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        _date = datetime.today()
        _dateFormat = _date.isoformat()
        _user = User(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(_user.id, "10111")
        self.assertEqual(_user.created_at, _date)
        self.assertEqual(_user.updated_at, _date)


class Test_Save(unittest.TestCase):
    '''Unittests for save function in User class.'''

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
        _user= User()
        sleep(0.1)
        f_updated_at = _user.updated_at
        _user.save()
        self.assertLess(f_updated_at, _user.updated_at)

    def test_double_save(self):
        _user = User()
        sleep(0.1)
        f_updated_at = _user.updated_at
        _user.save()
        s_updated_at = _user.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        _user.save()
        self.assertLess(s_updated_at, _user.updated_at)

    def test_args(self):
        _user = User()
        with self.assertRaises(TypeError):
            _user.save(None)

    def test_saveFileUpdates(self):
        _user = User()
        _user.save()
        _userid = "User." + _user.id
        with open("file.json", "r") as fl:
            self.assertIn(_userid, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unittests for to_dict function in User class.'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_keys_to_dict(self):
        _user = User()
        self.assertIn("id", _user.to_dict())
        self.assertIn("created_at", _user.to_dict())
        self.assertIn("updated_at", _user.to_dict())
        self.assertIn("__class__", _user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        _user = User()
        _user.middle_name = "Africa"
        _user.my_number = 23
        self.assertEqual("Africa", _user.middle_name)
        self.assertIn("my_number", _user.to_dict())

    def test_to_dict_datetime(self):
        _user = User()
        _user_dict = _user.to_dict()
        self.assertEqual(str, type(_user_dict["id"]))
        self.assertEqual(str, type(_user_dict["created_at"]))
        self.assertEqual(str, type(_user_dict["updated_at"]))

    def test_contrast_to_dict_(self):
        _user = User()
        self.assertNotEqual(_user.to_dict(), _user.__dict__)

    def test_args(self):
        _user = User()
        with self.assertRaises(TypeError):
            _user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
