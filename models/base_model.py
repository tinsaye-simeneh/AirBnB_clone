#!/usr/bin/python3

"""
This module contains the prototype for BaseModel class.
"""

import models
from uuid import uuid4
from datetime import datetime as dt


class BaseModel():
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = dt.utcnow()
            self.updated_at = dt.utcnow()
            models.storage.new(self)

    def __str__(self):
        """Prints : [<class name>] (<self.id>) <self.__dict__>"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime."""
        self.updated_at = dt.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        d = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                d[k] = dt.isoformat(v)
            else:
                d[k] = v
        d["__class__"] = self.__class__.__name__
        return d
