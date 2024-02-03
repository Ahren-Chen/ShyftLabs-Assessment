<!-- Courses view component -->
<template>
    <div class="container" style="align-items: center; justify-content: center; text-align: center;">
  
      <!-- Alert message if there is one to be shown -->
      <alert v-if="showAlert" :message="alertMessage" />
  
      <!-- Adding new courses button and refreshing courses button -->
      <div class="btn-group" role="group" aria-label="Basic example">
        <button @click="toggleAddCourseModal" class="btn btn-primary">Add Course</button>
        <button @click="getCourses" class="btn btn-secondary">Refresh</button>
      </div>
  
      <br><br>
  
      <!-- Table of courses -->
      <table class="table table-hover">
        <thead>
  
          <!-- Table columns -->
          <tr>
            <th scope="col">Course Name</th>
            <th></th>
          </tr>
        </thead>
  
        <!-- Table rows of courses -->
        <tbody>
          <tr v-for="(course, index) in courses" :key="index">
            <td>{{ course.course_name }}</td>
            <td>
              <div class="btn-group" role="group">
  
                <!-- Update and delete buttons -->
                <button type="button" class="btn btn-warning btn-sm" @click="toggleUpdateCourse(
                  course.course_name,
                  course.id
                )">Update
                </button>
                <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteCourse(course.id)">Delete</button>
  
              </div>
            </td>
          </tr>
        </tbody>
      </table>
  
      <!-- add new course form -->
      <div ref="addCourseModal" class="modal fade"
        :class="{ show: activeAddCourseModal, 'd-block': activeAddCourseModal }" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
  
              <!-- Add course title -->
              <h5 v-if="!updatingCourse" class="modal-title"> Add a new course </h5>
              <h5 v-if="updatingCourse" class="modal-title"> Update course </h5>
  
              <!-- Close button -->
              <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="toggleAddCourse">
                <span aria-hidden="true">&times;</span>
              </button>
  
            </div>
  
            <div class="modal-body">
              <form>
  
                <!-- Form field: Course Name-->
                <div class="mb-3">
                  <label for="addCourseCourseName" class="form-label">Course Name:</label>
                  <input type="text" class="form-control" id="addCourseCourseName" v-model="addCourseForm.course_name"
                    placeholder="Enter Course Name">
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
      <div v-if="activeAddCourseModal" class="modal-backdrop fade show"></div>
    </div>
  </template>
    
  <script>
  import axios from 'axios';
  import Alert from './Alert.vue';
  export default {
    name: 'Courses',
    data() {
      return {
        // List of courses
        courses: [],
  
        // Begin form for adding courses
        activeAddCourseModal: false,
  
        // Whether the form is for adding or updating a course
        updatingCourse: false,
  
        // The id of the course being updated
        updatingCourseId: null,
  
        // Whether to show the alert message or not
        showAlert: false,
  
        // The alert message to be shown
        alertMessage: '',

        // Form fields for adding a course
        addCourseForm: {
          course_name: '',
        },
      };
    },
    methods: {
  
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
  
      // Add a course to the database
      addCourse(payload) {
        axios.post(`http://localhost:3000/courses`, payload)
          .then(() => {
            this.getCourses();
          })
          .catch(error => {
            console.log(error);
            this.getCourses();
          });
      },
  
      // Update a course in the database
      updateCourses(payload) {
        const id = this.updatingCourseId;
        axios.put(`http://localhost:3000/courses/${id}`, payload)
          .then((response) => {
            this.getcourses();
            console.log(response.data.message)
          })
          .catch(error => {
            console.log(error);
            this.getCourses();
          });
      },
  
      // Delete a course from the database
      handleDeleteCourse(id) {
        axios.delete(`http://localhost:3000/courses/${id}`)
          .then(() => {
            this.getCourses();
          })
          .catch(error => {
            console.log(error);
            this.getCourses();
          });
  
        this.alertMessage = 'Course deleted successfully'
        this.showAlert = true;
      },
  
      // Reset the form fields
      handleAddReset() {
        this.initForm();
      },
  
      // Submit the form to add a course
      handleAddSubmit() {
  
        // Close the form
        this.toggleAddCourseModal();
  
        // Get the form fields
        let course_name = this.addCourseForm.course_name;
  
        if (!course_name) {
          this.alertMessage = 'Please fill in all fields'
          this.showAlert = true;
          this.initForm();
          return;
        }
  
        // Create the payload and load course information
        const payload = {
          course_name: course_name
        };
  
        // If the course is being updated, update the course, otherwise add the course
        if (this.updatingCourseId != null && this.updatingCourse) {
          this.updateCourses(payload);
          this.alertMessage = 'Course updated successfully'
        }
        else {
          this.addCourse(payload);
          this.alertMessage = 'Course added successfully'
        }
  
        // Reset the form fields and show the alert message
        this.initForm();
        this.showAlert = true;
        this.updatingCourse = false;
        this.updatingCourseId = null;
      },
  
      // Initialize the form fields or reset them to empty
      initForm() {
        this.addCourseForm.course_name = '';
      },
  
      // Initialize the form fields for updating a course with existing information
      updateCourseFormInit(course_name) {
        this.addCourseForm.course_name = course_name;
      },
  
      // Toggle the add course modal
      toggleAddCourseModal() {
        const body = document.querySelector('body');
        this.activeAddCourseModal = !this.activeAddCourseModal;
        this.showAlert = false;
        this.alertMessage = '';
        if (this.activeAddCourseModal) {
          body.classList.add('modal-open');
        } else {
          body.classList.remove('modal-open');
        }
      },
  
      // Toggle the add course process
      toggleAddCourse() {
        this.updatingCourse = false;
        this.updatingCourseId = null;
        this.toggleAddCourseModal();
        this.initForm();
      },
  
      // Toggle the update course process
      toggleUpdateCourse(course_name, id) {
        this.updatingCourse = true;
        this.updatingCourseId = id;
        this.toggleAddCourseModal();
        this.updateCourseFormInit(course_name);
      },
    },
    components: {
      alert: Alert,
    },
    created() {
      this.getCourses();
    },
  };
  </script>