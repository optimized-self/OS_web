import os

from flask import Flask

from .activity.api import bp as activity_api

def create_app():
    app = Flask(__name__)

    app.register_blueprint(activity_api)

    return app

