<template>
  <div class="bg-dark p-5">
    <div class="container-fluid">
      <h3 class="text-light text-center list-title">
        {{ title }}
      </h3>

      <div class="table-responsive" v-if="games.length">
        <table class="table table-dark table-hover text-center">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Title</th>
              <th scope="col">Release Date</th>
              <th scope="col">Consoles</th>
              <th scope="col">Genres</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in games" v-bind:key="value.id">
              <th scope="row">{{ key + 1 }}</th>
              <td>{{ value.title }}</td>
              <td>{{ value.year }}</td>
              <td>
                <span
                  v-for="(value, key) in value.consoles"
                  :key="key"
                  class="badge rounded-pill m-1"
                  :class="'bg-' + consoles[value.name]"
                >
                  {{ value.name }}
                </span>
              </td>
              <td>
                <span
                  v-for="(value, key) in value.genres"
                  :key="key"
                  class="badge rounded-pill m-1"
                  :class="'bg-' + genres[value.name]"
                >
                  {{ value.name }}
                </span>
              </td>

              <td>
                <router-link :to="value.link" class="btn btn-primary m-2">
                  <i class="bi bi-box-arrow-up-right"></i>
                </router-link>

                <router-link
                  :to="'/edit-game/' + value.game_id"
                  class="btn btn-success m-2"
                >
                  <i class="bi bi-pencil-square"></i>
                </router-link>

                <router-link
                  :to="'/delete-game/' + value.game_id"
                  class="btn btn-danger m-2"
                >
                  <i class="bi bi-trash"></i>
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { consoles } from "./consoles";
import { genres } from "../Genre/genres";

export default {
  name: "GameList",

  props: {
    title: {
      type: String,
      default: "All Games",
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
      games: [],
      consoles,
      genres,
    };
  },

  methods: {
    getGames() {
      axios
        .get(
          `http://localhost:5000/api/games?limit=${this.limit}&order_by=${this.orderBy}&order=${this.order}&offset=${this.offset}`
        )
        .then((response) => {
          this.games = response.data;

          this.games.map((game) => {
            game.link = `/games/${game.game_id}`;
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getGames();
  },
};
</script>
