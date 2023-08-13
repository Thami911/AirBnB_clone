#!/usr/bin/python3
"""Describes the class for Amenity."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Presents the Amenity model.
    Attributes:
        name (str): The name of the amenity.
    """
    
    name = ""
