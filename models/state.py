#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """
        def class
        """
        variable = models.storage.all()
        list_city = []
        res = []
        for k in variable:
            c = k.replace('.', ' ')
            c = shlex.split(c)
            if (c[0] == 'City'):
                list_city.append(variable[k])
        for var in list_city:
            if (var.state_id == self.id):
                res.append(var)
        return (res)
