from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


students = [
    {
        'id': uuid.uuid4().hex,
        'first_name': 'John',
        'family_name': 'Doe',
        'date_of_birth': '1990/01/01',
    },
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Adding new students
@app.route('/students', methods=['GET', 'POST'])
def all_students():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        students.append({
            'id': uuid.uuid4().hex,
            'first_name': post_data.get('first_name'),
            'family_name': post_data.get('family_name'),
            'date_of_birth': str(post_data.get('date_of_birth')),
        })
        response_object['message'] = 'Student added!'
    else:
        response_object['students'] = students

    return jsonify(response_object)

# Updating students

def remove_student(student_id):
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            return True
    return False

@app.route('/students/<student_id>', methods=['PUT'])
def single_student(student_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        if not remove_student(student_id):
            response_object['message'] = 'Student not found!'
            return jsonify(response_object)
        
        students.append({
            'id': uuid.uuid4().hex,
            'first_name': post_data.get('first_name'),
            'family_name': post_data.get('family_name'),
            'date_of_birth': str(post_data.get('date_of_birth')),
        })
        response_object['message'] = 'Student updated!'
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()