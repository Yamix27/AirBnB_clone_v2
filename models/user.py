#!/usr/bin/python3
"""
Module: user.py

Defines the User class, a subclass of BaseModel.

The User class represents users
in the AirBnB clone project.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """
    User class for representing users
    in the AirBnB clone project.

    Attributes:
        email (str): Email address of the user.
        password (str): Password associated with the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        places: relationsship to the Place class.
        reviews: relationship to the Review class.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
