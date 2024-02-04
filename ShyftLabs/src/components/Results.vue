<template>
    <div class="container" style="align-items: center; justify-content: center; text-align: center;">

        <!-- Alert message if there is one to be shown -->
        <alert v-if="showAlert" :message="alertMessage" />

        <!-- Adding new results button and refreshing results button -->
        <div class="btn-group" role="group" aria-label="Basic example">
            <button @click="toggleAddResultModal" class="btn btn-primary">Add Result</button>
            <button @click="getResults" class="btn btn-secondary">Refresh</button>
        </div>

        <br><br>

        <!-- Table of results -->
        <table class="table table-hover">
            <thead>

                <!-- Table columns -->
                <tr>
                    <th scope="col">Course</th>
                    <th scope="col">Student</th>
                    <th scope="col">Score</th>
                    <th></th>
                </tr>
            </thead>

            <!-- Table rows of results -->
            <tbody>
                <tr v-for="(result, index) in results" :key="index">
                    <td>{{ result.course_name }}</td>
                    <td>{{ result.student_name }}</td>
                    <td>{{ result.score }}</td>
                    <td>
                        <div class="btn-group" role="group">

                            <!-- Update and delete buttons -->
                            <button type="button" class="btn btn-warning btn-sm" @click="toggleUpdateResult(
                                result.course_name,
                                result.student_name,
                                result.score,
                                result.id,
                            )">Update
                            </button>
                            <button type="button" class="btn btn-danger btn-sm"
                                @click="handleDeleteResult(result.id)">Delete</button>

                        </div>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- add new result form -->
        <div ref="addResultModal" class="modal fade"
            :class="{ show: activeAddResultModal, 'd-block': activeAddResultModal }" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">

                        <!-- Add result title -->
                        <h5 v-if="!updatingResult" class="modal-title"> Add a new result </h5>
                        <h5 v-if="updatingResult" class="modal-title"> Update results </h5>

                        <!-- Close button -->
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleAddResult">
                            <span aria-hidden="true">&times;</span>
                        </button>

                    </div>

                    <div class="modal-body">
                        <form>

                            <!-- Form field: Course Name-->
                            <div class="mb-3">
                                <label for="addResultCourseName" class="form-label">Course Name:</label>
                                <select class="form-select" id="addResultCourseName" v-model="addResultForm.course_name">
                                    <option v-for="course in courses" :key="course.id" :value="course.course_name">
                                        {{ course.course_name }}
                                    </option>
                                </select>
                            </div>

                            <!-- Form field: Student Name-->
                            <div class="mb-3">
                                <label for="addResultStudentName" class="form-label">Student Name:</label>
                                <select class="form-select" id="addResultStudentName" v-model="addResultForm.student_name">
                                    <option v-for="student in students" :key="student.id" :value="student.first_name + ` ` + student.family_name">
                                        {{ student.first_name + " " + student.family_name }}
                                    </option>
                                </select>
                            </div>

                            <!-- Form field: Score-->
                            <div class="mb-3">
                                <label for="addResultScore" class="form-label">Score:</label>
                                <select class="form-select" id="addResultScore" v-model="addResultForm.score">
                                    <option v-for="score in scores" :key="score" :value="score">
                                        {{ score }}
                                    </option>
                                </select>
                            </div>

                            <!-- Submit and reset buttons -->
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="handleAddSubmit">
                                    Submit
                                </button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleAddReset">
                                    Reset
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="activeAddResultModal" class="modal-backdrop fade show"></div>
    </div>
</template>
    
<script>
import axios from 'axios';
import Alert from './Alert.vue';
export default {
    name: 'Results',
    data() {
        return {
            // List of results
            results: [],

            // List of students
            students: [],

            // List of courses
            courses: [],

            // List of possible scores
            scores: ['A', 'B', 'C', 'D', 'E', 'F'],

            // Begin form for adding results
            activeAddResultModal: false,

            // Whether the form is for adding or updating a result
            updatingResult: false,

            // The id of the result being updated
            updatingResultId: null,

            // Whether to show the alert message or not
            showAlert: false,

            // The alert message to be shown
            alertMessage: '',

            // Form fields for adding a result
            addResultForm: {
                course_name: '',
                student_name: '',
                score: '',
            },
        };
    },
    methods: {
        // Get all students from the database
        getStudents() {
            axios.get(`http://localhost:3000/students`)
                .then(response => {
                    this.students = response.data.students;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        // Get all courses from the database
        getCourses() {
            axios.get(`http://localhost:3000/courses`)
                .then(response => {
                    this.courses = response.data.courses;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        // Get all results from the database
        getResults() {
            axios.get(`http://localhost:3000/results`)
                .then(response => {
                    this.results = response.data.results;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        // Add a result to the database
        addResult(payload) {
            axios.post(`http://localhost:3000/results`, payload)
                .then(() => {
                    this.getResults();
                })
                .catch(error => {
                    console.log(error);
                    this.getResults();
                });
        },

        // Update a result in the database
        updateResult(payload) {
            const id = this.updatingResultId;
            axios.put(`http://localhost:3000/results/${id}`, payload)
                .then((response) => {
                    this.getResults();
                    console.log(response.data.message)
                })
                .catch(error => {
                    console.log(error);
                    this.getResults();
                });
        },

        // Delete a result from the database
        handleDeleteResult(id) {
            axios.delete(`http://localhost:3000/results/${id}`)
                .then(() => {
                    this.getResults();
                })
                .catch(error => {
                    console.log(error);
                    this.getResults();
                });

            this.alertMessage = 'Result deleted successfully'
            this.showAlert = true;
        },

        // Reset the form fields
        handleAddReset() {
            this.initForm();
        },

        // Submit the form to add a result
        handleAddSubmit() {

            // Close the form
            this.toggleAddResultModal();

            // Get the form fields
            let course_name = this.addResultForm.course_name;
            let student_name = this.addResultForm.student_name;
            let score = this.addResultForm.score;
            console.log(course_name, student_name, score)
            if (!course_name || !student_name || !score) {
                this.alertMessage = 'Please fill in all fields'
                this.showAlert = true;
                this.initForm();
                return;
            }

            // Create the payload and load results information
            const payload = {
                course_name: course_name,
                student_name: student_name,
                score: score,
            };

            // If the result is being updated, update the results, otherwise add the result
            if (this.updatingResultId != null && this.updatingResult) {
                this.updateResult(payload);
                this.alertMessage = 'Result updated successfully'
            }
            else {
                this.addResult(payload);
                this.alertMessage = 'Result added successfully'
            }

            // Reset the form fields and show the alert message
            this.initForm();
            this.showAlert = true;
            this.updatingResult = false;
            this.updatingResultId = null;
        },

        // Initialize the form fields or reset them to empty
        initForm() {
            this.addResultForm.course_name = '';
            this.addResultForm.student_name = '';
            this.addResultForm.score = '';
        },

        // Initialize the form fields for updating a result with existing information
        updateResultFormInit(course_name, student_name, score) {
            this.addResultForm.course_name = course_name;
            this.addResultForm.student_name = student_name;
            this.addResultForm.score = score;
        },

        // Toggle the add result modal
        toggleAddResultModal() {
            const body = document.querySelector('body');
            this.activeAddResultModal = !this.activeAddResultModal;
            this.showAlert = false;
            this.alertMessage = '';
            if (this.activeAddResultModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
        },

        // Toggle the add result process
        toggleAddResult() {
            this.toggleAddResultModal();
            this.updatingResult = false;
            this.updatingResultId = null;
            this.initForm();
        },

        // Toggle the update result process
        toggleUpdateResult(course_name, student_name, score, id) {
            this.toggleAddResultModal();
            this.updatingResult = true;
            this.updatingResultId = id;
            this.updateResultFormInit(course_name, student_name, score);
        },
    },
    components: {
        alert: Alert,
    },
    created() {
        this.getResults();
        this.getStudents();
        this.getCourses();
    },
};
</script>