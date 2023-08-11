#!/usr/bin/python3
"""Describes the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Shows an abstracted storage engine.
    Attributes:
        __file__obj (str): The name of the file to save objects to.
        __obj (dict): A dictionary of instantiated objects.
    """
    __file__obj = "file.json"
    __obj = {}

    def all(self):
        """Return the dictionary __obj."""
        return FileStorage.__obj

    def new(self, obj):
        oj_name = obj.__class__.__name__
        FileStorage.__obj["{}.{}".format(oj_name, obj.id)] = obj

    def save(self):
        ox_dict = FileStorage.__obj
        obj_dict = {obj: ox_dict[obj].to_dict() for obj in ox_dict.keys()}
        with open(FileStorage.__file__obj, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file__obj) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

