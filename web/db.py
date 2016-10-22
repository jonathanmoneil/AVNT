#!/usr/bin/env python
''' insert some data into the database '''

from conf import *
import json
from pymongo import MongoClient
import time

DB_NAME = 'avnt'
DB_COLLECTION = 'data'

def _connect_db():
    # Connect to the DB
    db_client = MongoClient(DB_HOST)
    db_connect = db_client[DB_NAME]
    return db_connect
    
def put_stuff_in_db():
    # Insert some stuff into the database
    db_client = _connect_db()
    result_insert = db_client.DB_COLLECTION.insert_one({
        "Created by": "jmo",
        "Created": time.time(),
        "City": "Chicago",
        "State": "Illinois"
    })
    return

def query_db():
    # Fetch data from db
    db_client = _connect_db()
    query_result = db_client.DB_COLLECTION.find_one()
    return query_result

if __name__ == '__main__':
    put_stuff_in_db()
