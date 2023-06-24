#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from uuid import uuid4
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes"""

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict.pop("_sa_instance_state", None)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
