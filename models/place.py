#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os
import shlex


place_amenity = Table("place_amenity", Base.metadata, Column("place_id",
                      String(60), ForeignKey("places.id"), primary_key=True,
                      nullable=False), Column("amenity_id", String(60),
                      ForeignKey("amenitites.id"), primary_key=True,
                      nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 Back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """
            return reviews
            """
            variable = models.storage.all()
            review_list = []
            res = []
            for k in variable:
                rev = k.replace('.', ' ')
                rev = shlex.split(rev)
                if (rev[0] == 'Review'):
                    review_list.append(variable[k])
            for var in review_list:
                if (var.place_id == self.id):
                    res.append(var)
            return (res)

        @property
        def amenities(self):
            """
            return amenities
            """
            res = self.amenity_ids
            return res

        @amenities.setter
        def amenities(self, obj=None):
            """
            add amenities tto id
            """
            if obj is not None and isinstance(obj, Amenity) and \
                    obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
