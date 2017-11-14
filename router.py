from flask import Flask, jsonify
from models.student import Student

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def root():
    return 'Endpoint not used!'

@app.route('/healthcheck')
def healthcheck():
    return 'ok'

Student.add_routes(app)
