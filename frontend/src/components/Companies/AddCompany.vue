<template>
  <TitleDisplay title="Add Company" />
  <div class="bg-dark p-5 text-light">
    <div class="container">
      <form class="row g-3" @submit.prevent="show">
        <div class="col-md-6">
          <label for="inputEmail4" class="form-label">Name</label>
          <input
            type="text"
            class="form-control"
            id="inputEmail4"
            placeholder="Title"
            name="name"
          />
        </div>
        <div class="col-md-6">
          <label for="inputPassword4" class="form-label">Foundation Year</label>
          <input
            type="number"
            class="form-control"
            id="inputPassword4"
            placeholder="Year"
            name="foundation_year"
          />
        </div>

        <div class="col-md-6">
          <label for="inputCity" class="form-label">Country</label>
          <input
            type="text"
            class="form-control"
            id="inputEmail4"
            placeholder="Contry..."
            name="country"
          />
        </div>

        <div class="col-12">
          <button type="submit" class="btn btn-primary">Add Company</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import TitleDisplay from "../common/TitleDisplay.vue";
import axios from "axios";

export default {
  name: "AddCompany",

  components: {
    TitleDisplay,
  },

  methods: {
    show(event) {
      const formData = new FormData(event.target);
      const data = Object.fromEntries(formData);

      const isValid = this.checkInputs();

      console.log(isValid);

      if (!isValid) return;

      axios
        .post("http://localhost:5000/api/company", data)
        .then((response) => {
          console.log(response);
          this.$router.push("/companies");
        })
        .catch((error) => {
          console.log(error);
        });
    },

    checkInputs() {
      const inputs = document.querySelectorAll(".form-control");

      let isValid = true;

      inputs.forEach((input) => {
        if (input.value === "") {
          input.classList.add("is-invalid");
          isValid = false;
        } else {
          input.classList.remove("is-invalid");
        }
      });

      return isValid;
    },
  },
};
</script>
