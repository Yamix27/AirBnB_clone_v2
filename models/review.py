#!/usr/bin/python3
"""
Module: review.py

Defines the Review class, a subclass of BaseModel.

The Review class represents reviews of places in
the AirBnB clone project.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Review class for representing reviews of places
    in the AirBnB clone project.

    Attributes:
        text (str): The review text.
        place_id (str): ID of the place being reviewed.
        user_id (str): ID of the review writer.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
