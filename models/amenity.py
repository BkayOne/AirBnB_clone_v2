#!/usr/bin/python3
"""This is the amenity class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

# Check if place_amenity table is already defined
metadata = Base.metadata
if 'place_amenity' not in metadata.tables:
    place_amenity = Table(
        'place_amenity',
        metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
    )


class Amenity(BaseModel, Base):
    """This is the class for Amenity"""

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity', backref="amenities")

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)
