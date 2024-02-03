<template>
    <div>
      <!-- Showing alerts for any message /> -->
      <div class="alert alert-info" role="alert">{{ message }}</div>
      <br/>
    </div>
  </template>
  
  <script>
  export default {
    props: ['message'],
  };
  </script>