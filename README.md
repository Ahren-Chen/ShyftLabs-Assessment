# ShyftLabs-Assessment

## Objective

- Creating a single paged application for Student Result Management System

## Home Page

- Must include a navigation bar on the left side of the page
- Must include a link to the Home Page
- Must include a link to the Students Page

## Students Page

- Must provide a form with First Name, Family Name, Date of birth, and a submit button
- When submitting, all fields mult be filled
- When submitting, the date of birth must be a valid date
- When submitting, the student must be at least 10 years old
- After all requirements are fulfilled, student is added to the database, inputs are cleared, and a confirmation notification appears
- Users can see a list of all stored students that updates after every new addition of a student

## Courses Page

- Must provide a form with Course Name and a submit button
- When submitting all fields must be filled
- After all requirements are fulfilled, course is added to the data base, inputs are cleared, and a confirmation notification appears
- Users can see a list of all stored courses that updates after every new addition of a course

## Results Page

- Must provide a form with course name, student name, and score fields as a dropdown box
- When submitting, all fields must be filled
- After all requirements are fulfilled, the results are added to the data base, inputs are cleared, and a confirmation notification appears
- Users can see a list of all stored results that updates after every new addition of a result

## Dependencies
- Python 3.12.0
- Flask 3.0.1
- Flask-Cors-4.0.0
- npm 8.19.3
- Node v18.13.0
- Vue 3.9.2
- Axios 1.6.7
- Bootstrap 5.3.2

Note: There is also a requirements.txt file with all pip installs in the server folder

## Running Project

1. Activate the python virtual environment in the `server` folder using `source env/Scripts/activate` with a gitbash application
2. Activate the flask application by using `flask run --port=3000 --debug`
3. Open up another gitbash applicaiton and activate the virtual environment
4. Go to the `ShyftLabs` folder 
5. run `npm install`
6. run `npm run dev`
7. Head to [local host ](http://localhost:5173/)