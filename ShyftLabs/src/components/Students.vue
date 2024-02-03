<template>
  <div class="container" style="align-items: center; justify-content: center; text-align: center;">
    <alert v-if="showAlert" :message="alertMessage" />
    <div class="btn-group" role="group" aria-label="Basic example">
      <button @click="toggleAddStudentModal" class="btn btn-primary">Add Student</button>
      <button @click="getStudents" class="btn btn-secondary">Refresh</button>
    </div>
    <br><br>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">First Name</th>
          <th scope="col">Family Name</th>
          <th scope="col">Date of Birth</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(student, index) in students" :key="index">
          <td>{{ student.first_name }}</td>
          <td>{{ student.family_name }}</td>
          <td>{{ student.date_of_birth }}</td>
          <td>
            <div class="btn-group" role="group">
              <button type="button" class="btn btn-warning btn-sm" @click="toggleUpdateStudent(
                student.first_name,
                student.family_name,
                student.date_of_birth,
                student.id
                )">Update
              </button>
              <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteStudent(student.id)">Delete</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- add new book modal -->
    <div
      ref="addStudentModal"
      class="modal fade"
      :class="{ show: activeAddStudentModal, 'd-block': activeAddStudentModal }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new student</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddStudent">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addStudentFirstName" class="form-label">First Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addStudentFirstName"
                  v-model="addStudentForm.first_name"
                  placeholder="Enter First Name">
              </div>
              <div class="mb-3">
                <label for="addStudentLastName" class="form-label">Family Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addStudentLastName"
                  v-model="addStudentForm.family_name"
                  placeholder="Enter Family Name">
              </div>
              <div class="mb-3">
                <label for="addStudentDOB" class="form-label">Date of Birth:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addStudentDOB"
                  v-model="addStudentForm.date_of_birth"
                  placeholder="YYYY/MM/DD">
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddStudentModal" class="modal-backdrop fade show"></div>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  import Alert from './Alert.vue';
  export default {
    name: 'Students',
    data() {
      return {
        students: [],
        activeAddStudentModal: false,
        updatingStudent: false,
        updatingStudentId: null,
        showAlert: false,
        alertMessage: '',
        addStudentForm: {
          first_name: '',
          family_name: '',
          date_of_birth: ''
        },
      };
    },
    methods: {
        getStudents() {
            axios.get(`http://localhost:3000/students`)
            .then(response => {
                this.students = response.data.students;
            })
            .catch(error => {
                console.log(error);
            });
        },
        addStudent(payload) {
            axios.post(`http://localhost:3000/students`, payload)
            .then(() => {
                this.getStudents();
            })
            .catch(error => {
                console.log(error);
                this.getStudents();
            });
        },
        updateStudent(payload) {
            const id = this.updatingStudentId;
            axios.put(`http://localhost:3000/students/${id}`, payload)
            .then((response) => {
                this.getStudents();
                console.log(response.data.message)
            })
            .catch(error => {
                console.log(error);
                this.getStudents();
            });
        },

        handleDeleteStudent(id) {
          axios.delete(`http://localhost:3000/students/${id}`)
          .then(() => {
            this.getStudents();
          })
          .catch(error => {
            console.log(error);
            this.getStudents();
          });

          this.alertMessage = 'Student deleted successfully'
          this.showAlert = true;
        },

        handleAddReset() {
          this.initForm();
        },

        handleAddSubmit() {
          this.toggleAddStudentModal();

          let first_name = this.addStudentForm.first_name;
          let family_name = this.addStudentForm.family_name;

          if (!first_name || !family_name) {
            this.alertMessage = 'Please fill in all fields'
            this.showAlert = true;
            this.initForm();
            return;
          }

          let date = ''
          const validDate = /^\d{4}\/\d{2}\/\d{2}$/
          if (validDate.test(this.addStudentForm.date_of_birth)) {
            date = this.addStudentForm.date_of_birth
          } else {
            this.showAlert = true;
            this.alertMessage = 'Please enter a valid date of birth in the format YYYY/MM/DD'
            this.initForm();
            return
          }

          const currentDate = new Date()

          //Check if the date is actually a valid date
          const [year, month, day] = date.split('/').map(Number)
          if (month < 1 || month > 12 || day < 1 || day > 31) {
            this.showAlert = true;
            this.alertMessage = 'Please enter a valid date of birth in the format YYYY/MM/DD'
            this.initForm();
            return
          }
          else if (month == 2 && day > 29) {
            this.showAlert = true;
            this.alertMessage = 'Please enter a valid date of birth in the format YYYY/MM/DD'
            this.initForm();
            return
          }
          else if (month == 2 && day > 28 && year % 4 != 0) {
            this.showAlert = true;
            this.alertMessage = 'Please enter a valid date of birth in the format YYYY/MM/DD'
            this.initForm();
            return
          }
          else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
              this.showAlert = true;
              this.alertMessage = 'Please enter a valid date of birth in the format YYYY/MM/DD'
              this.initForm();
              return
            }
          }
          const inputDate = new Date(date)
          
          if (inputDate > currentDate) {
            this.showAlert = true;
            this.alertMessage = 'Date of birth cannot be in the future'
            this.initForm();
            return
          }
          else if (!inputDate) {
            this.showAlert = true;
            this.alertMessage = 'Please enter a valid date of birth in the format YYYY/MM/DD'
            this.initForm();
            return
          }
          const ageInMilliseconds = currentDate - inputDate;
          const ageInYears = ageInMilliseconds / (365.25 * 24 * 60 * 60 * 1000); // Approximate days in a year
          if (ageInYears < 10) {
            this.showAlert = true;
            this.alertMessage = 'Students must be at least 10 years old to be added to the database'
            this.initForm();
            return
          }

          const payload = {
            first_name: first_name,
            family_name: family_name,
            date_of_birth: date,
          };

          if (this.updatingStudentId != null && this.updatingStudent) {
            this.updateStudent(payload);
            this.alertMessage = 'Student updated successfully'
          }
          else {
            this.addStudent(payload);
            this.alertMessage = 'Student added successfully'
          }
          this.initForm();
          this.showAlert = true;
        },

        initForm() {
          this.addStudentForm.first_name = '';
          this.addStudentForm.family_name = '';
          this.addStudentForm.date_of_birth = '';
        },

        updateStudentFormInit(first_name, family_name, date_of_birth) {
          this.addStudentForm.first_name = first_name;
          this.addStudentForm.family_name = family_name;
          this.addStudentForm.date_of_birth = date_of_birth;
        },

        toggleAddStudentModal() {
          const body = document.querySelector('body');
          this.activeAddStudentModal = !this.activeAddStudentModal;
          this.showAlert = false;
          this.alertMessage = '';
          if (this.activeAddStudentModal) {
            body.classList.add('modal-open');
          } else {
            body.classList.remove('modal-open');
          }
        },

        toggleAddStudent() {
          this.toggleAddStudentModal();
          this.updatingStudent = false;
          this.updatingStudentId = null;
          this.initForm();
        },

        toggleUpdateStudent(first_name, family_name, date_of_birth, id) {
          this.toggleAddStudentModal();
          this.updatingStudent = true;
          this.updatingStudentId = id;
          this.updateStudentFormInit(first_name, family_name, date_of_birth);
        },
    },
    components: {
      alert: Alert,
    },
    created() {
        this.getStudents();
    },
  };
  </script>