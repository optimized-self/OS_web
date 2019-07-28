import os
import json

from pymongo import MongoClient
from urllib import parse

def insert_one(collection_name, document):
    try:
        # get the collection object
        client = MongoClient(os.environ.get('DB_CONNECTION_STRING'))
        db = client[os.environ['DB_NAME']]
        collection = db[collection_name]
       
        # insert the document into the collection
        collection.insert_one(document)

        # pymongo added a (unserializable) ObjectId to the document
        # scrub it and return the id so the user may use it if they wish
        id = document.pop('_id', None)

        return str(id) 
    except UnicodeError as err:
        print(f"UnicodeError: {err}")

    return False
