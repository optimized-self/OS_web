import os
import json

from pymongo import MongoClient
from urllib import parse

def insert_one(collection_name, document):
    try:
        # get the collection object
        client = MongoClient(_get_db_connection_string())
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

def _get_db_connection_string():
    user = parse.quote_plus(os.environ['DB_USER'])
    with open(os.environ['DB_PASSWORD_FILE']) as f:
        password = parse.quote_plus(f.readline().rstrip('\n'))
    host = parse.quote_plus(os.environ['DB_HOST_NAME'])
    port = parse.quote_plus(os.environ['DB_HOST_PORT'])
    db_connection_string = f"mongodb://{user}:{password}@{host}:{port}"
    return db_connection_string
