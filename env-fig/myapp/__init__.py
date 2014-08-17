# -*- coding: utf-8 -*-
"""
    myapp
    ~~~
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:%s/%s' % (
    os.environ['DB_1_ENV_POSTGRESQL_USER'],
    os.environ['DB_1_ENV_POSTGRESQL_PASS'],
    os.environ['DB_1_PORT_5432_TCP_ADDR'],
    os.environ['DB_1_PORT_5432_TCP_PORT'],
    os.environ['DB_1_ENV_POSTGRESQL_DB'])

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    db.session.add(User())
    db.session.commit()
    return 'index'
