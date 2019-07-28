import os
from flask import Flask
from flask_restful import Resource, Api

#instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# register blueprints
from project.api import activity_blueprint
app.register_blueprint(activity_blueprint)
