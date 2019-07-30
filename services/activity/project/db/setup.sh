#!/bin/sh

PYTHON_DB_PASSWORD=$(cat $PYTHON_DB_PASSWORD_FILE)

mongo admin --eval "db.createUser({user: 'python', pwd: '$PYTHON_DB_PASSWORD', roles:[{role:'readWrite', db:'optimized_self'}]});"
