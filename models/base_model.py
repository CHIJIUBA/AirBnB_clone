#!/usr/bin/python3
"""Defines a base model class."""
import uuid
from datetime import datetime


class BaseModel:
    """Represent the base model.

    defines all common attributes/methods for other classes.

    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Base model.

        Args:
            **kwargs (dict): The identity of the new Base.
            *args(any): The identity of the new Base
        """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                elif key == "name":
                    self.name = value
                elif key == "my_number":
                    self.my_number = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the print() and str() representation the basemodel."""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates the updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary representation of the basemodel."""
        self_dict = self.__dict__
        self_dict["__class__"] = type(self).__name__
        self_dict["created_at"] = str(datetime
                                      .isoformat(self.created_at))
        self_dict["updated_at"] = str(datetime
                                      .isoformat(self.updated_at))
        return self_dict
