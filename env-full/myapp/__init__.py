# -*- coding: utf-8 -*-
"""
    myapp
    ~~~
"""

from flask import Flask

from utils import init_logger

app = Flask(__name__)

init_logger(app)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/error')
def err():
    raise Exception('Something bad happened!')
