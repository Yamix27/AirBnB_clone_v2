#!/usr/bin/python3
"""
Module: city.py

Defines the City class, a subclass of BaseModel.

The City class represents a city
in the AirBnB clone project.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """
    City class for representing cities
    in the AirBnB clone project.

    Attributes:
        state_id (str): ID of the State.
        name (str): Name of the city.
        places: relationship to the Place class.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
