"""_summary_
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
