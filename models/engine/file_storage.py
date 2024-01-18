#!/usr/bin/python3
"""
implementation of the FileStorage class.
"""
import json
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class FileStorage:
    """
    This class handles the serialization of instances
    to a JSON file and the deserialization of a JSON file
    to an instances.

    Attributes:
        __file_path: The path to the JSON file.
        __objects: The objects to be stored.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        return a dictionary.

        Return:
            return a dictionary of __object.
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """
        sets __object to given object.

        Args:
            obj: given object.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serialize the file path to JSON file path.
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserialize the JSON file.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete an existing element by its object.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """
        calls reload() method.
        """
        self.reload()
