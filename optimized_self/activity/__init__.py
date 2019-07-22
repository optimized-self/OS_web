from flask import Blueprint
from flask_restful import Api

from .api import Activity

bp = Blueprint('activity_api', __name__, url_prefix='/api')
api = Api(bp)

api.add_resource(Activity, '/activity')
