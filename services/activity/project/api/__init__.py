from flask import Blueprint
from flask_restful import Api

from .activity import Activity

activity_blueprint = Blueprint('activity_api', __name__, url_prefix='/api')
api = Api(activity_blueprint)

api.add_resource(Activity, '/activity')
