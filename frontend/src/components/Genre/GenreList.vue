<template>
  <div class="bg-dark p-5">
    <div class="container-fluid">
      <h3 class="text-light text-center list-title">
        {{ title }}
      </h3>

      <div class="table-responsive" v-if="genres.length">
        <table class="table table-dark table-hover text-center">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Description</th>
              <th scope="col">Games</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in genres" v-bind:key="value.genre_id">
              <th scope="row">{{ key + 1 }}</th>
              <td>{{ value.name }}</td>
              <td>{{ value.description }}</td>
              <td>{{ value.games.length }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GenreList",

  props: {
    title: {
      type: String,
      default: "All Genres",
    },
    limit: {
      type: Number,
      default: 0,
    },
    orderBy: {
      type: String,
      default: "title",
    },
    order: {
      type: String,
      default: "asc",
    },
    offset: {
      type: Number,
      default: 0,
    },
  },

  data() {
    return {
      genres: [],
    };
  },

  methods: {
    getGenres() {
      axios
        .get(`http://localhost:5000/api/genre`)
        .then((response) => {
          this.genres = response.data;

          this.genres.map((genre) => {
            genre.link = `/genres/${genre.genre_id}`;
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getGenres();
  },
};
</script>
