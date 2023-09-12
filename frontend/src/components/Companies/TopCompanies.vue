<template>
  <div class="bg-dark p-5">
    <div class="container">
      <h3 class="text-light company-title text-center list-title">
        Top Companies
      </h3>
      <div class="table-responsive">
        <table class="table table-dark table-hover text-center">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Title</th>
              <th scope="col">Foundation Year</th>
              <th scope="col">Country</th>
              <th scope="col">Games in Play Pulse</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in companies" v-bind:key="value.id">
              <th scope="row">{{ key + 1 }}</th>
              <td>{{ value.name }}</td>
              <td>{{ value.foundation_year }}</td>
              <td>{{ value.country }}</td>
              <td>{{ value.games.length }}</td>
              <td>
                <a class="btn btn-primary" :href="value.link"> See more </a>
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

export default {
  name: "TopCompanies",
  data() {
    return {
      companies: null,
    };
  },
  created: async function () {
    this.companies = await axios
      .get("http://localhost:5000/api/company/top")
      .then((response) => (this.companies = response.data));

    this.companies.map((company) => {
      company.link = "/companies/" + company.company_id;
    });
  },
};
</script>

<style></style>
