#!/usr/bin/python3
"""This is the city class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """This is the class for City"""

    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
