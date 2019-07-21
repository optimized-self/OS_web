from flask_restful import reqparse

# initialize the parser
post_parser = reqparse.RequestParser()
post_parser.add_argument('name')

def parse_args():
    return post_parser.parse_args()
