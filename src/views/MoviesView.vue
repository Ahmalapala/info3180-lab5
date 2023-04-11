<template>
    <div class="container">
      <h1 class="my-4">Movies</h1>
      <div class="row">
        <div class="col-md-4" v-for="movie in movies" :key="movie.id">
          <div class="card mb-4">
            <img class="card-img-top" :src="movie.poster" alt="Movie Poster">
            <div class="card-body">
              <h2 class="card-title">{{ movie.title }}</h2>
              <p class="card-text">{{ movie.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  let movies = ref([]);
  
  function fetchMovies() {
    fetch('/api/v1/movielist')
      .then(response => response.json())
      .then(data => {
        movies.value = data.movies;
      })
      .catch(error => {
        console.log('There was a problem with the fetch operation:', error);
      });
  }
  
  onMounted(() => {
    fetchMovies();
  });
  </script>
  