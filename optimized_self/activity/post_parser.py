from flask_restful import reqparse
from datetime import datetime

# initialize the parser
post_parser = reqparse.RequestParser()

post_parser.add_argument(
    name='name',
    required=True,
)
post_parser.add_argument(
    name='time_start',
    default=datetime.utcnow()
)
post_parser.add_argument(
    name='time_end',
    default=datetime.utcnow()
)

def parse_args():
    return post_parser.parse_args()
