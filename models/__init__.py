#!/usr/bin/python3
"""
module instantiates an object of class DBStorage
if the environment variable HBNB_TYPE_STORAGE is equal to db or
This module instantiates an object of class Storage
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
