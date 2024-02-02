<template>
    <div class="container">
        <button @click="getStudents" class="btn btn-primary">Refresh</button>
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
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'Students',
    data() {
      return {
        students: [],
      };
    },
    methods: {
        getStudents() {
            axios.get('http://localhost:3000/students')
            .then(response => {
                this.students = response.data.students;
            })
            .catch(error => {
                console.log(error);
            });
        }
    },
    created() {
        this.getStudents();
    },
  };
  </script>