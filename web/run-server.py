#!/usr/bin/env python
''' Start flask server '''

from conf import *
from db import update_views, query_db
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def render_index():
    return 'OK, server is up!'

@app.route('/db')
def db_results():
    update_views()
    query_result = query_db() 
    if query_result is None:
        result = 'Unable to find data in the database!'
        return result
    else: 
        return query_result
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
