#!/usr/bin/env python
''' Start flask server '''

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/query')
def query_db():
    # query the db for the thing
    pass
