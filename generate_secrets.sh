#!/bin/bash

# make secrets directory if it doesn't already exist
mkdir secrets -p

# generate activity-db root password
openssl rand -base64 48 > secrets/activity-db_root_password.txt

# generate activity-db python password
openssl rand -base64 48 > secrets/activity-db_python_password.txt
