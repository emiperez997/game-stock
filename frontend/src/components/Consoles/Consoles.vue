<template>
  <div class="bg-dark p-5">
    <div class="container-fluid">
      <h3 class="text-light text-center list-title">
        {{ title }}
      </h3>

      <div class="table-responsive" v-if="consoles.length">
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
            <tr v-for="(value, key) in consoles" v-bind:key="value.genre_id">
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
  name: "Consoles",

  props: {
    title: {
      type: String,
      default: "All Consoles",
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
      consoles: [],
    };
  },

  methods: {
    getConsoles() {
      axios
        .get(`http://localhost:5000/api/console`)
        .then((response) => {
          this.consoles = response.data;

          this.consoles.map((console) => {
            console.link = `/consoles/${console.console_id}`;
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getConsoles();
  },
};
</script>
