#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
import unittest
import mysql.connector
import MySQLdb
import os
from models.state import State



class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "file", "Only applicable for DB storage")
    def test_create_state(self):
        # 1. Get initial state count (using raw MySQL connection)
        db = MySQLdb.connect(
        host=os.getenv("HBNB_MYSQL_HOST"),
        user=os.getenv("HBNB_MYSQL_USER"),
        password=os.getenv("HBNB_MYSQL_PWD"),
        database=os.getenv("HBNB_MYSQL_DB"),
        )
        # cursor = conn.cursor()
        cursor1 = db.cursor()
        
        # cursor.execute("SELECT COUNT(*) FROM states")
        cursor1.execute("SELECT COUNT(*) FROM states")
        # initial_count = cursor.fetchone()[0]
        init_count = cursor1.fetchone()[0]
        
        # conn.close()
        cursor1.close()
        db.close()

        # 2. Create a State object and save it (using your storage engine logic)
        state = State(name="California")
        state.save()

        # 3. Get state count after creation
        # conn = mysql.connector.connect(  # Re-establish connection
        #     # ... same connection details
        # )
        db = MySQLdb.connect(
        host=os.getenv("HBNB_MYSQL_HOST"),
        user=os.getenv("HBNB_MYSQL_USER"),
        password=os.getenv("HBNB_MYSQL_PWD"),
        database=os.getenv("HBNB_MYSQL_DB"),
        )
        
        # cursor = conn.cursor()
        cursor1 = db.cursor()
        # cursor.execute("SELECT COUNT(*) FROM states")
        cursor1.execute("SELECT COUNT(*) FROM states")
        # final_count = cursor.fetchone()[0]
        final_count = cursor1.fetchone()[0]
        # conn.close()
        db.close()

        # 4. Assert count difference
        # self.assertEqual(final_count, initial_count + 1, "State not created in database")
        self.assertEqual(final_count, init_count + 1, "State not created in database")
