#!/usr/bin/python
""" contains the Amenity class definition"""
import sqlalchemy
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an instance of an amenity."""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new amenity instance."""
        super().__init__(*args, **kwargs)
