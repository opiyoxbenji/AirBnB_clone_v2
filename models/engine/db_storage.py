#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.ext.declarative import declarative_base
"""
Database storgage system
"""


storage_classes = [BaseModel, City, User, State, Place, Review, Amenity]


class DBStorage:
    """
    Database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initializer for database
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on database session
        """
        query_dict = {}
        if cls:
            query = self.__session.query(cls)
            for instance in query:
                key = "{}.{}".format(type(instance).__name__, instance.id)
                query_dict[key] = instance
        else:
            for c in storage_classes:
                query = self.__session.query(c)
                for instance in query:
                    key = "{}.{}".format(type(instance).__name__, instance.id)
                    query_dict[key] = instance
        return (query_dict)

    def new(self, obj):
        """
        adds new ovject to db
        """
        self.__session.add(obj)

    def save(self):
        """
        commit changes to current db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj from db
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables and current
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
