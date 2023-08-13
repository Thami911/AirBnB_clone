#!/usr/bin/python3
'''Review class definition'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class attributes

        Attributes:
            place_id (str): place's id
            user_id (str): user's id
            text (str): review message
    
    '''

    place_id = ""
    user_id = ""
    text = ""
