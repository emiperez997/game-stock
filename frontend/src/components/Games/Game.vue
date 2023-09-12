<template>
  <div>
    <TitleDisplay :title="game.title" />
    <div>
      <div class="d-flex justify-content-center bg-dark p-3">
        <img :src="game.images" alt="" style="width: 300px; height: auto" />
      </div>
      <div class="bg-dark p-2 text-light">
        <div class="container">
          <p><strong>Company:</strong> {{ company.name }}</p>
          <p><strong>Description:</strong> {{ game.description }}</p>
          <p><strong>Director: </strong> {{ game.director }}</p>
          <p>
            <strong>Genres: </strong> <br />
            <span
              v-for="(value, key) in game.genres"
              :key="key"
              class="badge rounded-pill m-1"
              :class="'bg-' + genres[value.name]"
            >
              {{ value.name }}
            </span>
          </p>
          <p>
            <strong>Consoles:</strong>
            <br />
            <span
              v-for="(value, key) in game.consoles"
              :key="key"
              class="badge rounded-pill m-1"
              :class="'bg-' + consoleColors[value.name]"
            >
              {{ value.name }}
            </span>
          </p>
          <p><strong>Release Date:</strong> {{ game.year }}</p>
          <p>
            <strong>Actions: </strong>
            <router-link
              :to="'/edit-game/' + game._id"
              class="btn btn-success m-2"
            >
              Edit
            </router-link>

            <router-link
              :to="'/delete-game/' + game._id"
              class="btn btn-danger m-2"
            >
              Delete
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { genres } from "../Genre/genres";
import { consoles as consoleColors } from "./consoles";
import TitleDisplay from "../common/TitleDisplay.vue";

export default {
  name: "Game",

  components: {
    TitleDisplay,
  },

  data() {
    return {
      game: {},
      genres: genres,
      company: {},
      consoles: {},
      consoleColors,
    };
  },

  methods: {
    getGame() {
      axios
        .get("http://localhost:5000/api/games/" + this.$route.params.id)
        .then((response) => {
          this.game = response.data;
          this.consoles = this.game.consoles;
          this.company = this.game.company;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getGame();
  },
};
</script>
