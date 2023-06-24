#!/usr/bin/python3
"""This module defines a class to manage the database storage for the application"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
# import other model classes here


class DBStorage:
    """This class manages the database storage"""
    
    __engine = None
    __session = None
    classes = {
        'State': State,
        # add other model classes here
    }
    
    def __init__(self):
        """Initialize the DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, database),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query all objects of a specified class from the database"""
        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = self.classes.get(cls, None)
            if cls:
                objects = {obj.id: obj for obj in self.__session.query(cls).all()}
        else:
            for cls in self.classes.values():
                objects.update({obj.id: obj for obj in self.__session.query(cls).all()})
        return objects
    
    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete the object from the current database session"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
