#!/usr/bin/python3
"""
Module: base_model.py

Defines the BaseModel class, the parent class for all
other classes in the AirBnB_clone_v2 project.
Handles instance initialization, serialization
and deserialization.

Classes:
- BaseModel: The base class for objects
in the AirBnB clone project.

Attributes:
- id (str): Unique identifier generated for each instance.
- created_at (datetime): Instance creation time.
- updated_at (datetime): Instance last update time.

Methods:
- __init__(self, *args, **kwargs): BaseModel constructor.
- __str__(self): Returns a string representation of the instance.
- save(self): Updates the instance's updated_at attribute and saves.
- to_dict(self): Return a dictionary instance for serialization.
- __repr__(self): Return a string representaion.
- delete current instance from storage.
"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """
    define the 'BaseModel' class.

    attributes:
        id (sqlalchemy String): 'BaseModel' id.
        created_at (sqlalchemy DateTime): creation date
        updated_at (sqlalchemy DateTime): update date
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """
        initialize a new BaseModel
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        return the string representation of the 'BaseModel' instance.

        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        return a string representaion.
        """
        return self.__str__()

    def save(self):
        """
        updates 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        return the dictionary representation of the BaseModel instance.

        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """
        delete current instance from storage.
        """
        models.storage.delete(self)
