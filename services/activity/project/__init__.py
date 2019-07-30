import os
from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

#instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# setup db connection
mongo = MongoEngine(app)

# register blueprints
from project.api import activity_blueprint
app.register_blueprint(activity_blueprint)
