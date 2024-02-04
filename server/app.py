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

courses = [
    {
        'id': uuid.uuid4().hex,
        'course_name': 'Math',
    }
]

results = [
    {
        'id': uuid.uuid4().hex,
        'student_name': 'John Doe',
        'course_name': 'Math',
        'score': 'A',
    }
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Adding new students ----------------------------------------------------------------------

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

# Updating students ----------------------------------------------------------------------

def remove_student(student_id):
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            return True
    return False

@app.route('/students/<student_id>', methods=['PUT', 'DELETE'])
def single_student(student_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(student_id)
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

    elif request.method == 'DELETE':
        if remove_student(student_id):
            response_object['message'] = 'Student removed!'
        else:
            response_object['message'] = 'Student not found!'
    return jsonify(response_object)

# Adding new courses ----------------------------------------------------------------------

@app.route('/courses', methods=['GET', 'POST'])
def all_courses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        courses.append({
            'id': uuid.uuid4().hex,
            'course_name': post_data.get('course_name'),
        })
        response_object['message'] = 'Course added!'
    else:
        response_object['courses'] = courses

    return jsonify(response_object)

# Updating courses ----------------------------------------------------------------------

def remove_course(course_id):
    for course in courses:
        if course['id'] == course_id:
            courses.remove(course)
            return True
    return False

@app.route('/courses/<course_id>', methods=['PUT', 'DELETE'])
def single_course(course_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(course_id)
        if not remove_course(course_id):
            response_object['message'] = 'Course not found!'
            return jsonify(response_object)
        
        courses.append({
            'id': uuid.uuid4().hex,
            'course_name': post_data.get('course_name'),
        })
        response_object['message'] = 'Course updated!'

    elif request.method == 'DELETE':
        if remove_course(course_id):
            response_object['message'] = 'Course removed!'
        else:
            response_object['message'] = 'Course not found!'
    return jsonify(response_object)

# Adding new results ----------------------------------------------------------------------
@app.route('/results', methods=['GET', 'POST'])
def all_results():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        results.append({
            'id': uuid.uuid4().hex,
            'student_name': post_data.get('student_name'),
            'course_name': post_data.get('course_name'),
            'score': post_data.get('score'),
        })
        response_object['message'] = 'Result added!'
    else:
        response_object['results'] = results

    return jsonify(response_object)

# Updating results ----------------------------------------------------------------------

def remove_result(result_id):
    for result in results:
        if result['id'] == result_id:
            results.remove(result)
            return True
    return False

@app.route('/results/<result_id>', methods=['PUT', 'DELETE'])
def single_result(result_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(result_id)
        if not remove_result(result_id):
            response_object['message'] = 'Result not found!'
            return jsonify(response_object)
        
        results.append({
            'id': uuid.uuid4().hex,
            'student_name': post_data.get('student_name'),
            'course_name': post_data.get('course_name'),
            'score': post_data.get('score'),
        })
        response_object['message'] = 'Result updated!'

    elif request.method == 'DELETE':
        if remove_result(result_id):
            response_object['message'] = 'Result removed!'
        else:
            response_object['message'] = 'Result not found!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()