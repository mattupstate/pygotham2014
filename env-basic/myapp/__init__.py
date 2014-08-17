# -*- coding: utf-8 -*-
"""
    myapp
    ~~~~~
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
