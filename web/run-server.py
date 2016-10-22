#!/usr/bin/env python
''' Start flask server '''

from conf import *
from db import query_db
from flask import Flask


app = Flask(__name__)

@app.route('/')
def render_index():
    return 'OK, server is up!'

@app.route('/db')
def db_results():
    query_result = query_db()
    result_str = ''.join('{}: {}\n'.format(key, val) for key, val in query_result.items())
    return result_str
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
