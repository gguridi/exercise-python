from ..models.student import Student

class TestStudent:

    class Request:
        form = {}

    @classmethod
    def setup_class(self):
        self.request = self.Request()
        self.request.form['name'] = 'TestName'
        self.request.form['surname'] = 'TestSurname'
        self.request.form['birthdate'] = 'TestBirthdate'

    @classmethod
    def teardown_class(self):
        del self.request

    def test_loading(self):
        student = Student()
        student.load_from_request(self.request)
        assert student.name == 'TestName'
        assert student.surname == 'TestSurname'
        assert student.birthdate == 'TestBirthdate'

