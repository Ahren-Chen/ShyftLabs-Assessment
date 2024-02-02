from flask import Flask, jsonify, request
from flask_cors import CORS


students = [
    {
        'first_name': 'John',
        'family_name': 'Doe',
        'date_of_birth': '01/01/1990',
    },
    {
        'first_name': 'Jeff',
        'family_name': 'Doe',
        'date_of_birth': '01/01/1990',
    },
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# test route
@app.route('/students', methods=['GET', 'POST'])
def all_students():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        students.append({
            'first_name': post_data.get('first_name'),
            'family_name': post_data.get('family_name'),
            'date_of_birth': post_data.get('date_of_birth'),
        })
        response_object['message'] = 'Student added!'
    else:
        response_object['students'] = students

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()