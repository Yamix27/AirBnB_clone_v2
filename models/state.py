#!/usr/bin/python3
"""
Module: state.py

Defines the State class, a subclass of BaseModel.

The State class represents states
in the AirBnB clone project.
"""
import models
import shlex
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """
    State class for representing states
    in the AirBnB clone project.

    Attributes:
        name (str): Name of the state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
