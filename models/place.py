#!/usr/bin/python3
"""This is the place class"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table

metadata = Base.metadata

place_amenity = Table(
    'place_amenity', metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """This is the class for Place"""

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, back_populates="place_amenities")
    reviews = relationship("Review", cascade="all, delete", backref="place")

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """getter attribute returns the list of Amenity instances"""
        return self.amenities

    @amenities.setter
    def amenities(self, obj):
        """setter attribute handles append method for adding an Amenity.id"""
        if type(obj) == Amenity:
            self.amenities.append(obj.id)
