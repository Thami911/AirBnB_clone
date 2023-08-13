#!/usr/bin/python3
"""User class definition"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class attributes

    Attributes:
            email (str): user's email
            password (str): user's password
            first_name (str): user's first name
            last_name (str): user's last name
        
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
