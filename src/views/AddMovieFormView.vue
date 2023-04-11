<template>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <h1>Add Movie</h1>
          <movie-form />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import MovieForm from "../components/MovieForm.vue";
  
  export default {
    name: "AddMovieFormView",
    components: { MovieForm }
  };
  </script>
  