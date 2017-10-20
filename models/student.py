from sqlalchemy import Column, Integer, String
from flask import request, jsonify
from base import Base, db


class Student(db.Model, Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    surname = Column(String(60))
    birthdate = Column(String(60))

    @staticmethod
    def create(flask_request):
        student = Student()
        student.load_from_request(flask_request)
        db.session.add(student)
        db.session.commit()
        return {'id': student.id, 'message': 'Student created successfully'}

    def update(self, flask_request):
        self.load_from_request(flask_request)
        db.session.commit()
        return {'message': 'Student updated successfully'}

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return {'message': 'Student deleted successfully'}

    def load_from_request(self, flask_request):
        self.name = flask_request.form['name']
        self.surname = flask_request.form['surname']
        self.birthdate = flask_request.form['birthdate']

    @staticmethod
    def add_routes(app):

        @app.route('/students', methods=['GET'])
        def route_list():
            return jsonify([student.serialize for student in Student.query.all()])

        @app.route('/student/<id>', methods=['GET'])
        def route_load(id):
            student = Student.query.get(id)
            return jsonify(student.serialize if student else {})

        @app.route('/student', methods=['POST'])
        def route_create():
            try:
                student = Student()
                info = student.create(request)
                return jsonify(action='success', **info)
            except Exception as e:
                return jsonify(action='failure', message=e.message)

        @app.route('/student/<id>', methods=['PUT'])
        def route_update(id):
            try:
                student = Student.query.get(id).update(request)
                return jsonify(action='success')
            except Exception as e:
                return jsonify(action='failure', message=e.message)

        @app.route('/student/<id>', methods=['DELETE'])
        def route_delete(id):
            try:
                Student.query.get(id).delete()
                return jsonify(action='success')
            except Exception as e:
                return jsonify(action='failure', message=e.message)

    def _to_jsonize(self):
        return ["id", "name", "surname", "birthdate"]

    def __repr__(self):
        return '<Student: {} {} {} {}>'.format(self.id, self.name, self.surname, self.birthdate)
