from flask import Flask, Blueprint
from flask_restful import Api, Resource

from optimized_self import db 
from .post_parser import parse_args

bp = Blueprint('activity_api', __name__, url_prefix='/api')
api = Api(bp)

class Activity(Resource):
    def get(self):
        return {'activity': 'Doing a Thing'}
    
    def post(self):
        args = parse_args()
        activity = {'name': args['name']}

        # insert the activity
        result = db.insert_one('activity', activity) 
        activity['id'] = result 

        return activity, 201


api.add_resource(Activity, '/activity')
