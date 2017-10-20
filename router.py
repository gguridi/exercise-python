from flask import Flask, jsonify
from models.base import db
from models.student import Student
from config import sqlalchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(sqlalchemy)
db.init_app(app)
db.create_all(app=app)

@app.route('/')
def root():
    return 'Endpoint not used!'

@app.route('/healthcheck')
def healthcheck():
    return 'ok'

Student.add_routes(app)
