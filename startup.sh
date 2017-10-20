#!/bin/bash

# Initialize python
cd /storage/app
make init

# Initialize jasmine properly
chmod +x tests_api/node_modules/jasmine-node/bin/jasmine-node

# Initialise database (attention, workaround for docker at the beginning)
find /var/lib/mysql -type f -exec touch {} \; && service mysql start
mysql -uroot -ptestpwd -e 'CREATE DATABASE IF NOT EXISTS soe;'
sleep 10

# Run the webservice
echo "Starting webservice..."
export FLASK_APP=router.py
python -m flask run --host=0.0.0.0
echo "Webservice initialized."
