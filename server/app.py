from flask import Flask, jsonify
from flask_cors import CORS

students = [
    {
        'first_name': 'John',
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
@app.route('/students', methods=['GET'])
def all_students():
    return jsonify({
        'status': 'success',
        'students': students
    })


if __name__ == '__main__':
    app.run()