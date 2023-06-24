#!/usr/bin/python3
"""This is the state class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """This is the class for State"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan",
                          passive_deletes=True)

    def __repr__(self):
        """Returns the string representation of the object."""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            {
                'name': self.name,
                'id': self.id,
                'updated_at': repr(self.updated_at),
                'created_at': repr(self.created_at)
            }
        )

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)
