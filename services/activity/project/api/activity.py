from flask_restful import Resource, fields, marshal_with

import project.db as db 
from .post_parser import parse_args

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
