from mongoengine import Document, StringField, DateTimeField
from project import mongo

import datetime

class Activity(mongo.Document):
    name       = mongo.StringField(max_length=200, required=True)
    time_start = mongo.DateTimeField(default=datetime.datetime.utcnow)
    time_end   = mongo.DateTimeField(default=datetime.datetime.utcnow)

