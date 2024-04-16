#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Create the database engine and establish a connection.
        """
        try:
            # Retrieve database credentials from environment variables
            user = getenv("HBNB_MYSQL_USER")
            pwd = getenv("HBNB_MYSQL_PWD")
            host = getenv("HBNB_MYSQL_HOST", "localhost")
            db = getenv("HBNB_MYSQL_DB")

            # Construct the connection URL with placeholders for sensitive data
            connection_url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"

            # Create the engine with connection pool pre-ping
            self.__engine = create_engine(connection_url, pool_pre_ping=True)

            # Drop all tables if HBNB_ENV is set to 'test'
            if getenv("HBNB_ENV") == "test":
                Base.metadata.drop_all(self.__engine)

        except OperationalError as e:
            print(f"Error connecting to database: {e}")
            exit(1)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes in the current database session.
        """
        try:
            self.__session.commit()
        except Exception as e:
            print(f"Error saving objects to database: {e}")
            self.__session.rollback()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
