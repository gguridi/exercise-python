const frisby = require('frisby');

const apiUrl = 'http://127.0.0.1:5000';

frisby.globalSetup({
    request: {
        inspectOnFailure: true,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }
});


describe('test suite for SoE API', function() {
    it('should list students', function(doneFn) {
        frisby.get(apiUrl + '/students')
            .expect('status', 200)
            .done(doneFn);
    })

    it('should create and delete users', function(doneFn) {
        let form = frisby.formData();
        form.append('name', 'FrisbyName');
        form.append('surname', 'FrisbySurname');
        form.append('birthdate', 'FrisbyBirthdate');

        frisby.post(apiUrl + '/student', { body: form })
            .expect('status', 200)
            .expect('json', {
                action: 'success'
            })
            .then(function(res) {
                studentId = res.json.id;
                return frisby.del(apiUrl + '/student/' + studentId)
                            .expect('status', 200)
            })
            .done(doneFn);
    })
})
