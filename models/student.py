import csv, random
from flask import request, jsonify
from base import Base


class Student(Base):

    filename = 'student.csv'

    id = ""
    name = ""
    surname = ""
    birthdate = ""

    @staticmethod
    def load():
        students = []
        with open(Student.filename, 'a+') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student = Student()
                student.load_from_csv(row)
                students.append(student)
        return students

    @staticmethod
    def save(students=[]):
        with open(Student.filename, 'a+') as csvfile:
            writer = csv.writer(csvfile)
            csvfile.truncate()
            for student in students:
                writer.writerow(student.to_array())

    @staticmethod
    def locate(id, students=[]):
        for index, student in enumerate(students):
            if id == student.id:
                return index
        return -1

    @staticmethod
    def get(id):
        students = Student.load()
        index = Student.locate(id, students)
        if index >= 0:
            return students[index]
        return None

    @staticmethod
    def create(flask_request):
        student = Student()
        student.load_from_request(flask_request)
        student.id = random.getrandbits(64)
        students = Student.load()
        students.append(student)
        Student.save(students)
        return {'id': student.id, 'message': 'Student created successfully'}

    def update(self, flask_request):
        self.load_from_request(flask_request)
        students = Student.load()
        index = Student.locate(self.id, students)
        if index >= 0:
            students[index] = self
        Student.save(students)
        return {'message': 'Student updated successfully'}

    def delete(self):
        students = Student.load()
        index = Student.locate(self.id, students)
        if index >= 0:
            students.pop(index)
        Student.save(students)
        return {'message': 'Student deleted successfully'}

    def load_from_request(self, flask_request):
        self.name = flask_request.form['name']
        self.surname = flask_request.form['surname']
        self.birthdate = flask_request.form['birthdate']

    def load_from_csv(self, row):
        self.id = row[0]
        self.name = row[1]
        self.surname = row[2]
        self.birthdate = row[3]

    def to_array(self):
        return [
            self.id,
            self.name,
            self.surname,
            self.birthdate
        ]

    @staticmethod
    def add_routes(app):

        @app.route('/students', methods=['GET'])
        def route_list():
            return jsonify([student.serialize for student in Student.load()])

        @app.route('/student/<id>', methods=['GET'])
        def route_load(id):
            student = Student.get(id)
            return jsonify(student.serialize if student else {})

        @app.route('/student', methods=['POST'])
        def route_create():
            try:
                info = Student.create(request)
                return jsonify(action='success', **info)
            except Exception as e:
                return jsonify(action='failure', message=e.message)

        @app.route('/student/<id>', methods=['PUT'])
        def route_update(id):
            try:
                student = Student.get(id).update(request)
                return jsonify(action='success')
            except Exception as e:
                return jsonify(action='failure', message=e.message)

        @app.route('/student/<id>', methods=['DELETE'])
        def route_delete(id):
            try:
                Student.get(id).delete()
                return jsonify(action='success')
            except Exception as e:
                return jsonify(action='failure', message=e.message)

    def _to_jsonize(self):
        return ["id", "name", "surname", "birthdate"]

    def __repr__(self):
        return '<Student: {} {} {} {}>'.format(self.id, self.name, self.surname, self.birthdate)
