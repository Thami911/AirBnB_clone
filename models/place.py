#!/usr/bin/python3
'''Place class definition'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Place class attributes

        Attributes:
        city_id (str): Id of the city
        user_id (str): user's id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms in the place
        number_bathrooms (int): number of bathrooms in the place
        max_guest (int): maximum number of guests allowed in the place
        price_by_night (int): cost per night of the place
        latitude (float): place's latitude coordinates
        longitude (float): place's longitude coordinates
        amenity_ids (list): list if amenity ids
    
    '''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
