<template>
    <div class="container">
        <button @click="getMessage" class="btn btn-primary">{{  msg  }}</button>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'Ping',
    data() {
      return {
        msg: 'Hello!',
      };
    },
    methods: {
        getMessage() {
            axios.get('http://localhost:3000/ping')
            .then(response => {
                this.msg = response.data;
            })
            .catch(error => {
                console.log(error);
            });
        }
    },
    created() {
        //this.getMessage();
    },
  };
  </script>