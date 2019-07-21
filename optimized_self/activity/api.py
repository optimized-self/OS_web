from flask import Flask, Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from optimized_self import db 
from .post_parser import parse_args

bp = Blueprint('activity_api', __name__, url_prefix='/api')
api = Api(bp)

activity_response_fields = {
    'name': fields.String,
    'time_start': fields.DateTime(),
    'time_end': fields.DateTime()
}

class Activity(Resource):
    def get(self):
        return {'activity': 'Doing a Thing'}
    
    @marshal_with(activity_response_fields)
    def post(self):
        activity = parse_args()

        # insert the activity
        result = db.insert_one('activity', activity) 
        activity['id'] = result 

        return activity, 201


api.add_resource(Activity, '/activity')
