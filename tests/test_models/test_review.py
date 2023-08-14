#!/usr/bin/python3
'''Unit tests for review class

Unittest classes:
    Test_Instantiation
    Test_Save
    Test_to_dict
'''
import unittest
import models
from models.review import Review
import os
from datetime import datetime
from time import sleep


class Test_Instantiation(unittest.TestCase):
    '''Unit tests for review class Instantiation'''

    def test_zero_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id(self):
        _review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(_review))
        self.assertNotIn("place_id", _review.__dict__)

    def test_user_id(self):
        _review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(_review))
        self.assertNotIn("user_id", _review.__dict__)

    def test_text(self):
        _review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(_review))
        self.assertNotIn("text", _review.__dict__)

    def test_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_double_created_at(self):
        review1= Review()
        sleep(0.1)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_double_updated_at(self):
        review1 = Review()
        sleep(0.1)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_unusedArgs(self):
        _review = Review(None)
        self.assertNotIn(None, _review.__dict__.values())

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        _date = datetime.today()
        _dateFormat = _date.isoformat()
        _review = Review(id="10111", created_at=_dateFormat, updated_at=_dateFormat)
        self.assertEqual(_review.id, "10111")
        self.assertEqual(_review.created_at, _date)
        self.assertEqual(_review.updated_at, _date)


class Test_Save(unittest.TestCase):
    '''Unittests for save function for Review class.'''

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
        _review = Review()
        sleep(0.1)
        f_updated_at = _review.updated_at
        _review.save()
        self.assertLess(f_updated_at, _review.updated_at)

    def test_double_save(self):
        _review = Review()
        sleep(0.1)
        f_updated_at = _review.updated_at
        _review.save()
        s_updated_at = _review.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        _review.save()
        self.assertLess(s_updated_at, _review.updated_at)

    def test_save_arg(self):
        _review = Review()
        with self.assertRaises(TypeError):
            _review.save(None)

    def test_updatesFile(self):
        _review = Review()
        _review.save()
        _reviewid = "Review." + _review.id
        with open("file.json", "r") as fl:
            self.assertIn(_reviewid, fl.read())


class Test_to_dict(unittest.TestCase):
    '''Unittests for to_dict function in Review class.'''

    def test_TypeOf_to_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_Keys_to_dict(self):
        _review = Review()
        self.assertIn("id", _review.to_dict())
        self.assertIn("created_at", _review.to_dict())
        self.assertIn("updated_at", _review.to_dict())
        self.assertIn("__class__", _review.to_dict())

    def test_extraAttributes_to_dict(self):
        _review = Review()
        _review.middle_name = "Africa"
        _review.my_number = 10
        self.assertEqual("Africa", _review.middle_name)
        self.assertIn("my_number", _review.to_dict())

    def test_to_dict_datetime(self):
        _review = Review()
        _review_dict = _review.to_dict()
        self.assertEqual(str, type(_review_dict["id"]))
        self.assertEqual(str, type(_review_dict["created_at"]))
        self.assertEqual(str, type(_review_dict["updated_at"]))

    def test_contrast_to_dict(self):
        _review = Review()
        self.assertNotEqual(_review.to_dict(), _review.__dict__)

    def test_to_dict_arg(self):
        _review = Review()
        with self.assertRaises(TypeError):
            _review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
