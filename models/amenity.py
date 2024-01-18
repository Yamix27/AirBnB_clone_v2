#!/usr/bin/python3
"""
Module: amenity.py

Defines the Amenity class, a subclass of BaseModel.

The Amenity class represents an amenity associated
with a place in the AirBnB clone project.
"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    Amenity class for representing amenities
    in the AirBnB clone project.

    Attributes:
        name (str): Amenity name.
        place_amenities: relationship to Place class.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
