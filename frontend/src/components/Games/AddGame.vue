<template>
  <TitleDisplay title="Add Game" />
  <div class="bg-dark p-5 text-light">
    <div class="container">
      <form class="row g-3" @submit.prevent="show">
        <div class="col-md-6">
          <label for="inputEmail4" class="form-label">Title</label>
          <input
            type="text"
            class="form-control"
            id="inputEmail4"
            placeholder="Title"
            name="title"
          />
        </div>
        <div class="col-md-6">
          <label for="inputPassword4" class="form-label">Year</label>
          <input
            type="number"
            class="form-control"
            id="inputPassword4"
            placeholder="Year"
            name="year"
          />
        </div>

        <div class="col-12">
          <div class="row">
            <div class="col-6">
              <label for="inputAddress" class="form-label">Director</label>
              <input
                type="text"
                class="form-control"
                id="inputAddress"
                placeholder="Director"
                name="director"
              />
            </div>
            <div class="col-6">
              <label for="inputAddress2" class="form-label">
                Cover Image
              </label>
              <input
                type="text"
                class="form-control"
                id="inputAddress2"
                name="image1"
                placeholder="Image URL"
              />
            </div>
          </div>
        </div>

        <div class="col-md-12">
          <label for="inputCity" class="form-label">Description</label>
          <textarea
            class="form-control"
            name="description"
            id=""
            cols="30"
            rows="10"
          ></textarea>
        </div>
        <div class="col-md-6">
          <label for="inputState" class="form-label">Consoles</label>
          <br />
          <ul class="list-group bg-dark text-dark">
            <li class="list-group-item" v-for="console in consoles">
              <input
                class="form-check-input me-1"
                type="checkbox"
                :name="console.name"
                id="firstCheckbox"
              />
              <label class="form-check-label" for="firstCheckbox">
                {{ console.name }}
              </label>
            </li>
          </ul>
        </div>

        <div class="col-md-6">
          <label for="inputState" class="form-label">Genres</label>
          <br />
          <ul class="list-group bg-dark text-dark">
            <li class="list-group-item" v-for="genre in genres">
              <input
                class="form-check-input me-1"
                type="checkbox"
                :name="genre.name"
                id="firstCheckbox"
              />
              <label class="form-check-label" for="firstCheckbox">
                {{ genre.name }}
              </label>
            </li>
          </ul>
        </div>
        <div class="col-md-6">
          <label for="inputState" class="form-label">Company</label>
          <select id="inputState" class="form-select" name="company_id">
            <option selected>Choose...</option>
            <option v-for="company in companies" :value="company.company_id">
              {{ company.name }}
            </option>
          </select>
        </div>

        <div class="col-12">
          <button type="submit" class="btn btn-primary">Add Game</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TitleDisplay from "../common/TitleDisplay.vue";

export default {
  name: "AddGame",
  data() {
    return {
      companies: [],
      game: [],
      genres: [],
      consoles: [],
    };
  },
  methods: {
    getCompanies() {
      axios
        .get("http://localhost:5000/api/company")
        .then((response) => {
          this.companies = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getGenres() {
      axios
        .get("http://localhost:5000/api/genre")
        .then((response) => {
          this.genres = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getConsoles() {
      axios
        .get("http://localhost:5000/api/console")
        .then((response) => {
          this.consoles = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    clearForm() {
      this.game = [];
    },

    show(e) {
      console.log(e.target);
      const formData = new FormData(e.target);

      this.checkForm(formData);

      // Get data from form
      const data = Object.fromEntries(formData.entries());

      const gameConsoles = this.consoles.filter((console) => {
        return data[console.name] === "on";
      });

      const gameGenres = this.genres.filter((genre) => {
        return data[genre.name] === "on";
      });

      this.game = {
        title: data.title,
        year: Number(data.year),
        director: data.director,
        images: [data.image1, data.image2, data.image3],
        videos: [],
        description: data.description,
        consoles: gameConsoles.map((console) => {
          return console.console_id;
        }),
        genres: gameGenres.map((genre) => {
          return genre.genre_id;
        }),
        company_id: Number(data.company_id),
      };

      // console.log(this.game);

      axios
        .post("http://localhost:5000/api/games", this.game)
        .then((response) => {
          console.log(response);
          e.target.reset();
          alert("Game added successfully");
        })
        .catch((error) => {
          console.log(error);
        });
    },

    checkForm(formData) {
      if (formData.get("title") === "") {
        alert("Please enter a title");
        return;
      }
      if (formData.get("year") === "") {
        alert("Please enter a year");
        return;
      }
      if (formData.get("director") === "") {
        alert("Please enter a director");
        return;
      }
      if (formData.get("image1") === "") {
        alert("Please enter an image");
        return;
      }
      if (formData.get("image2") === "") {
        alert("Please enter an image");
        return;
      }

      if (formData.get("description") === "") {
        alert("Please enter a description");
        return;
      }
      if (formData.get("consoles") === "") {
        alert("Please enter a console");
        return;
      }
      if (formData.get("company_id") === "") {
        alert("Please enter a company");
        return;
      }
    },
  },
  mounted() {
    this.getCompanies();
    this.getConsoles();
    this.getGenres();
  },

  components: { TitleDisplay },
};
</script>

<style>
textarea {
  resize: none;
}
</style>
