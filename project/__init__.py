# project/__init__.py

import os  # new
from flask import Flask, jsonify
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # new

import sys

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = app.config.from_object('project.config.DevelopmentConfig')  # new
app.config.from_object(app_settings)      # new

# instantiate the db
db = SQLAlchemy(app)  # new


# model
class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


#print(app.config, file=sys.stderr)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')
