<template>
    <form @submit.prevent="saveMovie" id="movieForm" enctype="multipart/form-data" method="post">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" v-model="formData.title">
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster Image</label>
        <input type="file" name="poster" class="form-control-file" @change="onPosterUpload">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
      <div v-if="message" class="mt-3 alert alert-success">{{ message }}</div>
      <div v-if="errorMessage" class="mt-3 alert alert-danger">{{ errorMessage }}</div>
    </form>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  let csrf_token = ref("");
  
  const formData = ref({
    title: '',
    description: '',
    poster: null,
  });
  
  let message = ref('');
  let errorMessage = ref('');

  function onPosterUpload(event) {
    formData.poster = event.target.files[0];
  }

onMounted(() => {
    getCsrfToken();
});

function getCsrfToken() {
 fetch('/api/v1/csrf-token')

    .then((response) => response.json())

    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })
 }
  
 async function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  console.log(movieForm)
  let form_data = new FormData(movieForm);
  console.log(form_data)

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {'X-CSRFToken': csrf_token.value}
  })
  .then(function (response) {
     if (!response.ok) {
       throw Error(response.statusText);
     }
     return response.json();
   })
   .then(function (data) {
     // display a success message
     console.log(data);
     message.value = 'Movie successfully saved!';
     errorMessage.value = '';
   })
   .catch(function (error) {
     console.log('There was a problem with the fetch operation:', error);
     errorMessage.value = 'Error saving movie';
     message.value = '';
   });
}


  </script>
  