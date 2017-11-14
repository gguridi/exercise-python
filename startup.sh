#!/bin/bash

# Initialize python
cd /storage/app
make init

# Initialize jasmine properly
chmod +x tests_api/node_modules/jasmine-node/bin/jasmine-node

# Run the webservice
echo "Starting webservice..."
export FLASK_APP=router.py
python -m flask run --host=0.0.0.0
echo "Webservice initialized."
