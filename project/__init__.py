# project/__init__.py

import os  # new
from flask import Flask, jsonify
from flask_restplus import Resource, Api

import sys

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = app.config.from_object('project.config.DevelopmentConfig')  # new
app.config.from_object(app_settings)      # new

print(app.config, file=sys.stderr)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')
