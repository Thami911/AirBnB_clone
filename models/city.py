#!/usr/bin/python3
'''City class definition'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City class attributes

        Attributes:
            state_id (str): state id
            name (str): City name
    '''

    state_id = ""
    name = ""
