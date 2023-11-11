"""_summary_
"""
from models.base_model import BaseModel


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
